import os

KB_PATH = "knowledge_base"

def retrieve_knowledge(email):

    email_lower = email.lower()

    if "password" in email_lower:
        file_name = "password_reset.txt"

    elif "charged" in email_lower or "billing" in email_lower:
        file_name = "billing.txt"

    elif "504" in email_lower or "api" in email_lower:
        file_name = "api_errors.txt"

    else:
        return "No relevant knowledge found."

    path = os.path.join(KB_PATH, file_name)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()