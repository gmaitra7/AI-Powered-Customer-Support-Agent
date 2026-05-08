AI-Powered Customer Support Agent

An AI-powered customer support workflow that automatically classifies customer emails, retrieves relevant knowledge, drafts responses, and escalates critical issues to human agents when required.

This project uses:

Python
OpenAI GPT models
Lightweight RAG (Retrieval-Augmented Generation)
Rule-based escalation logic

The system classifies:

Urgency
- Low
- Medium
- High
Topic
- Account
- Billing
- Bug
- Feature Request
- Technical Issue


Knowledge Retrieval (RAG)

The system retrieves relevant support documentation from a local knowledge base.

Example:

Billing issue → retrieves billing.txt
Password issue → retrieves password_reset.txt
AI Response Generation

The application generates:

professional
context-aware
grounded customer responses

using GPT and retrieved documentation.

Escalation Logic

The system escalates:

urgent issues
billing disputes
technical failures

to human support agents.

Workflow
Step 1 — Email Classification

GPT classifies:

urgency
support topic
Example

Input:

I was charged twice for my subscription.

Output:

{
  "urgency": "High",
  "topic": "Billing"
}
Step 2 — Knowledge Retrieval

The retriever searches the local knowledge base.

Example:

billing.txt
password_reset.txt
api_errors.txt
Step 3 — AI Response Generation

GPT generates a response using:

customer email
retrieved knowledge
Step 4 — Escalation Logic

The system escalates when:

urgency is High
topic is Billing
topic is Technical Issue

Example:

if urgency == "High":
    escalate = True
Example Input
Hi team,

I was charged twice this month for my subscription.
Please fix this immediately.

Thanks
Example Output
{
    "urgency": "High",
    "topic": "Billing",
    "response": "We sincerely apologize for the duplicate charge and understand your concern. Our billing team will review the issue immediately.",
    "escalate": true
}

ai-support-agent/
│
├── app/
│   ├── main.py
│   ├── classifier.py
│   ├── retriever.py
│   ├── responder.py
│   ├── escalation.py
│   └── config.py
│
├── knowledge_base/
│   ├── billing.txt
│   ├── password_reset.txt
│   └── api_errors.txt
│
├── requirements.txt
├── .env
└── README.md