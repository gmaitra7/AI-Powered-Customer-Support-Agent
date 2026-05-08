def should_escalate(classification):

    urgency = classification["urgency"]
    topic = classification["topic"]

    if urgency == "High":
        return True

    if topic in ["Billing", "Technical Issue"]:
        return True

    return False