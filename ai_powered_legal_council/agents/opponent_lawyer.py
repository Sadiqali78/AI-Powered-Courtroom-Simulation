from models.gemini_api import ask_gemini

def generate_counter_arguments(client_input):
    prompt = f"""You are acting as a professional opponent lawyer (defense/prosecutor) in a courtroom simulation.

Your task is to:
- Carefully analyze the client's claims below
- Identify weaknesses, false claims, or any violations of law
- Present strong, sharp, and logical counter-arguments
- Use accurate legal sections, terms, and principles wherever applicable
- Argue only based on law, evidence, and what actually happened in the scenario
- Speak in the tone and style of how a real courtroom lawyer would present an argument
- Make sure your reasoning is legally valid and understandable even to someone without legal knowledge

Client's Case Statement:
{client_input}

Now present your detailed and powerful counter-arguments, as if you were speaking in a courtroom.
"""
    return ask_gemini(prompt)
