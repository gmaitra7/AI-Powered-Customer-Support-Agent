from openai import OpenAI
from config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def classify_email(email):

    prompt = f"""
Classify this customer support email.

Return ONLY valid JSON.

Allowed urgency values:
- Low
- Medium
- High

Allowed topic values:
- Account
- Billing
- Bug
- Feature Request
- Technical Issue

Email:
{email}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    print("RAW GPT RESPONSE:")
    print(content)

    return json.loads(content)