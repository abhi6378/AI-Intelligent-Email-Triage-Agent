# 📧 AI Intelligent Email Triage Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Framework-orange)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-magenta)
![Gmail API](https://img.shields.io/badge/Google-Gmail%20API-red)
![License](https://img.shields.io/badge/License-MIT-green)

> **An autonomous multi-agent system that reads your Gmail inbox, intelligently categorizes emails, and drafts personalized, context-aware responses without human intervention.**

---

## 🚀 Project Overview

The **AI Intelligent Email Triage Agent** solves the problem of "Email Overload" by deploying a team of specialized AI agents to manage your inbox. Unlike basic auto-responders, this system understands context. It distinguishes between a VIP client asking for a meeting and a newsletter, drafting appropriate responses for each.

Built using **CrewAI** and **Google Gemini 2.5**, the system securely integrates with the **Gmail API** to fetch real emails and create drafts directly in your "Drafts" folder, ensuring a "Human-in-the-Loop" workflow for safety.

## ✨ Key Features

* **🤖 Multi-Agent Architecture:**
    * **Senior Analyst Agent:** Reads incoming emails, extracts sender metadata (Name, Email), and determines intent/urgency.
    * **Communications Specialist Agent:** Crafts professional, tone-appropriate responses based on the Analyst's insights.
* **🔐 Secure OAuth 2.0 Integration:** Connects directly to Gmail using Google's official API standards (no password sharing).
* **🧠 Intelligent Context Extraction:** Automatically cleans raw email headers (e.g., converts `"John Doe <john@gmail.com>"` to usable data) to personalize greetings.
* **✍️ Autonomous Drafting:** Instead of just printing text, the agents physically create draft emails in your Gmail account, ready for one-click sending.
* **⚡ High-Performance LLM:** Powered by Google's **Gemini 2.5 Flash-Lite** for speed and cost-efficiency.

---

## 🛠️ Tech Stack

* **Orchestration Framework:** [CrewAI](https://www.crewai.com/)
* **Large Language Model:** Google Gemini 2.5 Flash-Lite
* **Integration:** Google Gmail API (via `google-api-python-client`)
* **Authentication:** OAuth 2.0 (`google-auth-oauthlib`)
* **Language:** Python 3.x

---

## 🏗️ Architecture

The system follows a sequential multi-agent pipeline:

```text
[Gmail Inbox] 
      |
      v
(Tool: Fetch Unread Emails)
      |
      v
[Agent: Senior Analyst] ----> (Extracts Context & Intent)
      |
      v
[Agent: Writer] ------------> (Drafts Reply Content)
      |
      v
(Tool: Create Draft)
      |
      v
[Gmail Drafts Folder] ------> [User Review & Send]
⚙️ Installation & Setup
Prerequisites
Python 3.10 or higher.

A Google Cloud Project with Gmail API enabled.

Google Gemini API Key.

1. Clone the Repository
Bash

git clone [https://github.com/yourusername/ai-email-agent.git](https://github.com/yourusername/ai-email-agent.git)
cd ai-email-agent
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Environment Configuration
Create a .env file in the root directory and add your Google Gemini API key:

Code snippet

GOOGLE_API_KEY=your_gemini_api_key_here
4. Google Cloud Auth Setup
Go to Google Cloud Console.

Create a project and enable the Gmail API.

Configure OAuth Consent Screen (Set to External, add your email to Test Users).

Create OAuth 2.0 Client ID credentials (Select Desktop App).

Download the JSON file, rename it to credentials.json, and place it in the project root.

🚀 Usage
To start the agent, run the main script:

Bash

python main.py
First Run Behavior:

A browser window will open asking for permission to access your Gmail.

Click Allow (you may need to click "Advanced" -> "Go to App (Unsafe)" if in testing mode).

The agent will authenticate, check your inbox, and begin processing unread emails.

Check your Gmail Drafts folder to see the results!

🔮 Future Scope & Roadmap
We are actively working on scaling this project from a local script to a full-fledged SaaS product. Below are the planned development phases:

Phase 1: The "SaaS Product" (Streamlit Dashboard) 💻
Goal: Transition from a terminal-based interface to a user-friendly Web App.

Features:

A dashboard to view "Analyzed Emails" in a structured table.

Live editing of AI-generated drafts before approval.

"One-Click Send" button directly from the UI.

Phase 2: The "Executive Assistant" (Calendar Integration) 📅
Goal: Empower the agent to handle scheduling autonomously.

Features:

Integration with Google Calendar API.

Logic: If an email asks "Are you free Tuesday?", the agent checks real-time availability and drafts: "I am free at 2 PM or 4 PM."

Phase 3: The "Always-On" Worker (Automation) ⏱️
Goal: Convert the script into a 24/7 background service.

Features:

Deployment via Docker/Cloud Run with cron jobs running every 15 minutes.

Notification System: Sending alerts to Slack/WhatsApp (e.g., "I just drafted 3 urgent replies for you.") upon completing a cycle.

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License
Distributed under the MIT License. See LICENSE for more information.

Built with ❤️ by Abhishek