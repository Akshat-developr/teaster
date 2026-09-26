import os
import sys
from openai import OpenAI

# Initialize the OpenAI client pointing to xAI's endpoint
client = OpenAI(
    api_key=os.environ.get("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

# Maintain conversation memory
messages = [
    {
        "role": "system",
        "content": "You are a concise, helpful assistant. Keep responses focused and direct.",
    }
]

print("Grok Assistant initialized. Type 'quit' or 'exit' to stop.\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        # Append user turn to message history
        messages.append({"role": "user", "content": user_input})

        # Request streamed completion
        stream = client.chat.completions.create(
            model="grok-2-latest",  # or "grok-3", "grok-beta" depending on your access
            messages=messages,
            stream=True,
            temperature=0.7,
        )

        print("Grok: ", end="", flush=True)
        assistant_reply = []
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            print(delta, end="", flush=True)
            assistant_reply.append(delta)
        print("\n")

        # Save assistant's answer for multi-turn context
        messages.append({"role": "assistant", "content": "".join(assistant_reply)})

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}\n")
