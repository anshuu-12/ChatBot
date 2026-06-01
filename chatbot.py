import os
from google import genai
from google.genai import types

# Initialize the client. It automatically picks up the GEMINI_API_KEY environment variable.
try:
    client = genai.Client()
except Exception as e:
    client = None
    print(f"Initialization Error: Ensure GEMINI_API_KEY is set. Details: {e}")

def get_bot_response(user_message):
    """Sends the user's query to Gemini and returns the AI generated response."""
    if not client:
        return "System Error: API client is not configured. Please check your environment variables."
        
    if not user_message.strip():
        return "You didn't type anything!"

    try:
        # Use the fast, smart gemini-2.5-flash model for general, open-ended questions
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=types.GenerateContentConfig(
                # Optional: Give your chatbot a distinct personality
                system_instruction="You are a helpful, friendly, and brilliant web-based AI assistant.",
                temperature=0.7,
            )
        )
        return response.text
        
    except Exception as e:
        return f"Sorry, I encountered an error while processing your request: {str(e)}"
