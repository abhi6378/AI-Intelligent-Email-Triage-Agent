from crewai import Task

class EmailTasks:
    def categorize_email(self, agent):
        return Task(
            description="""
            1. Fetch emails.
            2. For each email, extract:
               - 'Sender Name': The human name (e.g. "John").
               - 'Sender Email': The clean address (e.g. "john@gmail.com").
               - 'Context': What do they want?
            """,
            agent=agent,
            expected_output="Structured list of Sender Name, Sender Email, and Context."
        )

    def draft_response(self, agent, analysis_output):
        return Task(
            description=f"""
            Use this analysis: {analysis_output}
            
            Draft a reply for each email.
            
            MANDATORY CHECKLIST:
            1. 'to_email' MUST be the clean email address.
            2. Subject MUST start with "Re: " + original subject.
            3. Salutation MUST use 'Sender Name' (e.g., "Hi John,").
            4. Sign-off MUST be:
               "Best regards,
                Abhishek"
            
            Use the 'Create Draft Reply' tool.
            """,
            agent=agent,
            expected_output="Confirmation of drafts created."
        )