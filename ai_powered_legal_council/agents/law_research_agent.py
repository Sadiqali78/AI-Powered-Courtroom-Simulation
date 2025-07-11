from models.gemini_api import ask_gemini

def retrieve_laws(client_input):
    prompt = f"""You are a Law Research Agent.

Based on the client's input below, find and explain the most relevant laws, legal sections, and past case precedents that apply to this situation.

Make sure your explanation is:
- Easy to understand for someone without legal knowledge
- Clear and accurate
- Covers the names of applicable sections and what they mean
- Written in a simple and non-technical manner

Client Situation:
{client_input}
"""
    return ask_gemini(prompt)
