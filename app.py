import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your API key from the .env file
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Endpoint for OpenRouter (uses OpenAI models like gpt-3.5-turbo)
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_ai_response(user_message):
    """
    Send the user's message to OpenRouter and get the AI's response.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # We are using OpenAI's gpt-3.5-turbo model via OpenRouter
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    # Send POST request to the OpenRouter API
    response = requests.post(API_URL, json=payload, headers=headers)

    # Extract and return the AI's message content
    if response.status_code == 200:
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "No response.")
    else:
        return f"Error: {response.status_code} - {response.text}"


def main():
    """
    Main loop to interact with the chatbot using text input.
    """
    print("🤖 OpenRouter Chatbot is ready. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        ai_reply = get_ai_response(user_input)
        print(f"AI: {ai_reply}")


if __name__ == "__main__":
    main()
# This script allows you to interact with OpenRouter's AI models using text input.
# Make sure to set your OpenRouter API key in the .env file before running this script.
