import os.path
import base64
import re  # New import for cleaning email addresses
from email.message import EmailMessage
from crewai.tools import tool
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']

class EmailTools:
    
    def _get_gmail_service():
        """Helper to authenticate and get the Gmail service."""
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return build('gmail', 'v1', credentials=creds)

    @tool("Check Inbox")
    def fetch_emails():
        """
        Fetches the last 3 unread emails.
        CRITICAL: Returns the raw 'From' string so the Agent can extract the name.
        """
        service = EmailTools._get_gmail_service()
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread", maxResults=3).execute()
        messages = results.get('messages', [])

        if not messages:
            return "No new emails found."

        email_list = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg['payload']['headers']
            
            subject = next((header['value'] for header in headers if header['name'] == 'Subject'), "No Subject")
            sender = next((header['value'] for header in headers if header['name'] == 'From'), "Unknown Sender")
            snippet = msg.get('snippet', '')
            
            email_list.append(f"Email ID: {message['id']} | Sender Raw: {sender} | Subject: {subject} | Content: {snippet}")

        return "\n\n".join(email_list)

    @tool("Create Draft Reply")
    def create_draft(email_id: str, subject: str, body: str, to_email: str):
        """
        Creates a DRAFT reply.
        IMPORTANT: 'to_email' must be a clean email address (e.g., bob@gmail.com).
        """
        try:
            # Clean up the email address (remove < > and names)
            clean_email = to_email
            email_match = re.search(r'<(.+?)>', to_email)
            if email_match:
                clean_email = email_match.group(1)
            
            service = EmailTools._get_gmail_service()
            
            message = EmailMessage()
            message.set_content(body)
            message['To'] = clean_email
            message['Subject'] = subject

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            create_message = {'message': {'raw': encoded_message}}
            
            draft = service.users().drafts().create(userId='me', body=create_message).execute()
            return f"SUCCESS: Draft created for {clean_email} (ID: {draft['id']})"
            
        except Exception as e:
            return f"ERROR creating draft: {str(e)}"