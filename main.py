from crewai import Crew, Process
from agents import EmailAgents
from tasks import EmailTasks

# 1. Instantiate the classes
agents = EmailAgents()
tasks = EmailTasks()

# 2. Define the Agents
# (The 'analyst' now has the tool to fetch real emails automatically)
analyst = agents.triage_agent()
writer = agents.writer_agent()

# 3. Define the Tasks
# Notice: We do NOT pass any email data here. 
# The Analyst Agent will use its 'Check Inbox' tool to go get the data.
task1 = tasks.categorize_email(analyst)

# Task 2 takes the output from Task 1 (the analysis) and drafts the response
task2 = tasks.draft_response(writer, task1)

# 4. Create the Crew
crew = Crew(
    agents=[analyst, writer],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential # Crucial: Analyst runs first, Writer runs second
)

print("## Starting the Real-Time Email Triage Crew ##")
print("-----------------------------------------------")
print("NOTE: If this is your first time, a browser window will open.")
print("Please log in with your Google Account to authorize the script.")
print("-----------------------------------------------")

# 5. Kickoff!
result = crew.kickoff()

print("\n\n########################")
print("## FINAL RESULT ##")
print("########################\n")
print(result)