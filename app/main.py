from classifier import classify_email
from retriever import retrieve_knowledge
from responder import generate_response
from escalation import should_escalate
import json

email = """
Hi team,

I was charged twice for my subscription.
Please fix this immediately.

Thanks
"""

# Step 1: Classification
classification = classify_email(email)

# Step 2: Retrieve Knowledge
knowledge = retrieve_knowledge(email)

# Step 3: Generate Response
response = generate_response(email, knowledge)

# Step 4: Escalation Decision
escalate = should_escalate(classification)

# Final Output
final_output = {
    "urgency": classification["urgency"],
    "topic": classification["topic"],
    "response": response,
    "escalate": escalate
}

print(json.dumps(final_output, indent=4))