import os

# from pprint import pprint
from dotenv import load_dotenv
from google import genai
from rich.pretty import pprint
from traccia import init, observe

load_dotenv()

init(api_key=os.getenv("TRACCIA_API_KEY"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_CANDIDATES = ["gemini-3.6-flash", "gemini-2.5-flash", "gemini-2.0-flash"]


# Tool call
@observe(name="get_weather", as_type="tool")
def get_weather(city: str) -> str:
    return f"The weather in {city} is 28°C and sunny."


# Tool Definition
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name",
                }
            },
            "required": ["city"],
        },
    }
]


# First interaction
def create_with_fallback(**kwargs):
    last_error: Exception | None = None
    for model in MODEL_CANDIDATES:
        try:
            return client.interactions.create(model=model, **kwargs)
        except Exception as e:
            print(f"Model '{model}' failed ({e}), trying next candidate...")
            last_error = e
    assert last_error is not None
    raise last_error


response = create_with_fallback(
    input="What is the weather in Sambalpur?",
    tools=tools,
)
model_used = response.model

# Handle tool calls
for item in response.steps:
    if item.type == "function_call":
        print("Tool called:", item.name)
        print("Arguments:", item.arguments)

        # item.arguments is already a dict
        result = get_weather(**item.arguments)

        print("Tool result:", result)

        response = client.interactions.create(
            model=model_used,
            previous_interaction_id=response.id,
            tools=tools,
            input=[
                {
                    "type": "function_result",
                    "name": item.name,
                    "call_id": item.id,
                    "result": [
                        {
                            "type": "text",
                            "text": result,
                        }
                    ],
                }
            ],
        )

print("\nFinal response:")

pprint(response)
