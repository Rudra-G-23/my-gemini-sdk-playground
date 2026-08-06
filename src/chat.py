import os

from dotenv import load_dotenv
from google import genai
from rich.pretty import pprint

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Explain money in a one line"
)

print("\n\n", interaction.output_text)

pprint(interaction)
