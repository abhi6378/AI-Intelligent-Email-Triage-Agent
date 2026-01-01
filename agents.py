import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from tools import EmailTools 

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    verbose=True,
    temperature=0.4, # Lower temp = less hallucination, more precision
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

class EmailAgents:
    def __init__(self):
        self.fetch_tool = EmailTools.fetch_emails
        self.draft_tool = EmailTools.create_draft

    def triage_agent(self):
        return Agent(
            role='Senior Email Analyst',
            goal='Extract the sender name and email clearly.',
            backstory="""You are a precise data analyst. 
            When you see "John Doe <john@gmail.com>", you explicitly separate 
            the name "John Doe" from the email "john@gmail.com".""",
            llm=llm,
            verbose=True,
            tools=[self.fetch_tool]
        )

    def writer_agent(self):
        return Agent(
            role='Personal Executive Assistant (Abhishek)',
            goal='Draft warm, personalized replies signing as Abhishek.',
            backstory="""You are the personal assistant to Abhishek. 
            
            RULES FOR WRITING:
            1. NEVER sign as "[Your Name]". ALWAYS sign as "Abhishek".
            2. NEVER address the user as "Dear Sender". extract their real name.
            3. If the email is professional, keep it brief.
            4. If the email is friendly, match the tone.
            """,
            llm=llm,
            verbose=True,
            tools=[self.draft_tool]
        )   