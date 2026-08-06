import os

from dotenv import load_dotenv
from openai import OpenAI
from rich.pretty import pprint

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explain Kubernetes in one line."}],
)

print(response.choices[0].message.content)

pprint("\n\n\n")
pprint(client)

pprint("\n\n\n")
pprint(response)
