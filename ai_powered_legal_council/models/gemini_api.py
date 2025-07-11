import os
import google.generativeai as genai

# Correct way to load the API key from an environment variable
genai.configure(api_key=os.getenv("your_google_api_key"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to interact with Gemini
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()
