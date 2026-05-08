from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(email, knowledge):

    prompt = f"""
    You are a professional customer support assistant.

    Customer Email:
    {email}

    Knowledge Base Information:
    {knowledge}

    Write a helpful professional response.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content