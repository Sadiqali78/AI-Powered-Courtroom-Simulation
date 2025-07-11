from models.gemini_api import ask_gemini

def analyze_logic(logic_report, laws):
    prompt = f"""You are a Logic Analyzer Agent.

Your task is to logically analyze the following case report and the related laws to simulate how a real-world legal reasoning engine would process this situation.

Please:
- Break down the arguments step-by-step
- Explain how the laws apply to each point
- Highlight logical strengths and weaknesses in the arguments
- Ensure your explanation is easy to follow, even for someone without legal or technical knowledge
- Maintain clarity, accuracy, and originality in your reasoning

Case Report:
{logic_report}

Relevant Laws:
{laws}

Now, provide a detailed and understandable logic-based analysis of this case:
"""
    return ask_gemini(prompt)
