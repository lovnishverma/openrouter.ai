import speech_recognition as sr
import requests
from gtts import gTTS
import os
import time
import re

# OpenRouter API Key (Get from https://openrouter.ai/)
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Initialize speech recognizer
recognizer = sr.Recognizer()

def get_ai_response(text):
    """Send user input to OpenAI/OpenRouter API and return the AI's response."""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": "openai/gpt-3.5-turbo", "messages": [{"role": "user", "content": text}]}
    
    response = requests.post(API_URL, json=data, headers=headers)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "I couldn't understand that.")

def speak(text):
    """Convert text to speech using gTTS."""
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Plays the response.mp3

def listen():
    """Capture user's voice input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Network error. Please check your internet.")
            return None

def wake_word_detected(text):
    """Detect the wake word 'Hey AI'."""
    return re.search(r"\bhey\sai\b", text, re.IGNORECASE)

def chatbot():
    """Main chatbot loop for voice interaction with Wake Word Activation."""
    print("🎙️ Voice Chatbot is Running! Say 'exit' to quit.")
    while True:
        user_input = listen()
        if user_input:
            # Check if the wake word is detected
            if wake_word_detected(user_input):
                speak("Hello, how can I assist you?")
                print("AI: Hello, how can I assist you?")
                time.sleep(2)  # Wait for a second before listening for the next input
            
            elif user_input.lower() == "exit":
                print("Goodbye!")
                speak("Goodbye!")
                break
            
            else:
                ai_response = get_ai_response(user_input)
                print(f"AI: {ai_response}")
                speak(ai_response)

if __name__ == "__main__":
    chatbot()
