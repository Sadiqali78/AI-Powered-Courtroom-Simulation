from models.gemini_api import ask_gemini

def provide_legal_advice(logic_report, laws):
    prompt = f"""You are a Legal Advisor Agent.

Based on the following case analysis and applicable laws, provide clear, legally accurate, and helpful advice to the client.

Ensure that your advice is:
- Easy to understand for someone with no legal background
- Based on real legal logic and applicable sections
- Original and clearly written
- Actionable and practical for the client to follow

Case Analysis:
{logic_report}

Relevant Laws:
{laws}

What legal advice would you give to the client in this situation?
"""
    return ask_gemini(prompt)
