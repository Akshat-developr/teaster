import os
import sys
from google import genai

# Initialize the client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Create a multi-turn chat session with a system instruction
chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": "You are a concise, helpful desktop assistant. Keep responses focused and direct."
    }
)

print("AI Assistant initialized. Type 'quit' or 'exit' to stop.\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        # Send message and stream the response
        response = chat.send_message_stream(user_input)
        print("Assistant: ", end="", flush=True)
        for chunk in response:
            print(chunk.text, end="", flush=True)
        print("\n")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}\n")
