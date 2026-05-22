# 🤖 OpenRouter API Chatbot: Introduction to APIs

Welcome to the OpenRouter API Chatbot project! This repository is designed to help students understand how to connect a Python application to a Large Language Model (LLM) using an Application Programming Interface (API). 

By utilizing [OpenRouter.ai](https://openrouter.ai/), we can access powerful AI models (like GPT-3.5) for free or at very low costs, making this an excellent, frugal approach to building production-ready AI applications.

## 🎯 Learning Objectives
By completing this project, you will learn:
1. What an API is and how to make POST requests using Python.
2. How to manage sensitive credentials (like API keys) securely using environment variables.
3. How to process JSON data returned by a web server.
4. How to build a simple Command Line Interface (CLI) loop.

---

## 📂 Project Structure

Understanding the anatomy of your project is the first step to becoming a good engineer. Here is what each file does:

* **`app.py`**: The main brain of our application. It contains the Python code that sends your messages to the AI and prints the response.
* **`requirements.txt`**: A list of external Python libraries our code depends on to run successfully.
* **`.env`**: A hidden configuration file where we safely store our secret API key so it doesn't get hardcoded into our main script.
* **`README.md`**: The instruction manual you are reading right now!

---

## 🚀 Step-by-Step Setup Guide

Follow these instructions to get your chatbot running locally.

### Step 1: Get Your Free API Key
Before writing any code, you need a "key" to unlock the API.
1. Visit [OpenRouter.ai](https://openrouter.ai/) and create an account.
2. Navigate to your account settings and generate a new API Key.
3. Copy this key (it usually starts with `sk-or-v1-...`). Keep it secret!

### Step 2: Install Dependencies
Open your terminal or command prompt, navigate to the project folder, and install the required libraries:
```bash
pip install -r requirements.txt

```

*(This installs `requests` for handling the API web calls and `python-dotenv` for reading our secret file).*

### Step 3: Configure Your Environment

1. In the root directory of the project, create a new file and name it exactly: `.env`
2. Open the `.env` file and paste your API key in the following format:

```env
OPENROUTER_API_KEY=your_actual_api_key_here

```

### Step 4: Run the Chatbot

Start the application by running the Python script:

```bash
python app.py

```

You should see `🤖 OpenRouter Chatbot is ready. Type 'exit' to quit.` appear in your terminal. Start typing to chat with the AI!

---

## 🧠 How the Code Works

If you look inside `app.py`, the most important part is the `get_ai_response()` function. Here is the breakdown of the API lifecycle:

1. **The Headers (Authentication):** We send our secret API key in the "Authorization" header to prove we have permission to use the server.
2. **The Payload (The Question):** We package the user's message into a structured format (JSON) that the OpenRouter server understands.
3. **The Request (The Delivery):** We use `requests.post()` to send our data to the API endpoint over the internet.
4. **The Response (The Answer):** The server sends back a massive chunk of data. We navigate through the JSON dictionary (`result.get("choices")[0]...`) to extract just the text we want to read.

---

*Happy Coding! Keep experimenting and building.*

```

```
