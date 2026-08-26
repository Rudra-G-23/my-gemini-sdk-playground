import sys

sys.path.append(r"C:\Users\sksam\OneDrive\Desktop\traccia-py")

from openai import OpenAI
from traccia import init, observe

# 1. Initialize Traccia (auto-patches OpenAI)
init(
    agent_id="llm_example",
    agent_name="LLM Example",
    api_key="tr_dev_myD9OVNCbSeAc35leyB",
    enable_console=True,
)

# 2. Initialize OpenAI client
# (Requires OPENAI_API_KEY environment variable to be set, or pass api_key="sk-...")
client = OpenAI()


# 3. Decorate LLM call function with as_type="llm"
@observe()
def generate_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5.4-mini", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    prompt = "Write a 2-sentence haiku about coding."
    print(f"Sending prompt to OpenAI: '{prompt}'\n")

    try:
        reply = generate_response(prompt)
        print(f"AI Response:\n{reply}")
    except Exception as e:
        print(f"Error making OpenAI call: {e}")
        print("\nNote: Make sure your OPENAI_API_KEY environment variable is set!")
