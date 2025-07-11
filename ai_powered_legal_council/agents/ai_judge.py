from models.gemini_api import ask_gemini

def give_verdict(client_input, legal_advice, counter_args):
    prompt = f"""Act as a fair and unbiased judge. Given:
    
Client Case:
{client_input}

Legal Advice:
{legal_advice}

Opponent Arguments:
{counter_args}

You must analyze and evaluate the statements, facts, and reasoning provided by all involved agents:
- Client Agent
- Law Research Agent
- Logic Analyzer Agent
- Legal Advisor Agent
- Opponent Agent

Based on their inputs, provide a valuable, well-reasoned, and original verdict that reflects real judicial thinking. Consider all perspectives carefully.

**Finally**, clearly state:
- 🏆 Who is the **winner** of the case
- ⚖️ Who is going to be **punished**
- 📜 What is the **punishment**, based on the final judgment

Ensure the decision is understandable to a non-legal person and reflects justice based on the arguments made by each agent."""
    
    return ask_gemini(prompt)
