# AI-Powered-Courtroom-Simulation
## 🚀 Features

- 📁 Multimodal document handling (PDF, TXT, PNG, JPG)
- 🧑 Client Agent: Presents the user's case
- 📚 Law Research Agent: Retrieves relevant legal info using Gemini LLM
- 🔍 Logic Analyzer: Checks internal logic and consistency
- 👨‍⚖️ Legal Advisor: Provides actionable legal insights
- 🗣️ Opponent Lawyer Agent: Simulates counter-arguments
- 🏛️ AI Judge: Evaluates all and delivers final verdict

---

## 📂 Folder Structure

```
ai_powered_legal_council/
├── main.py
├── requirements.txt
├── interface/
│   └── ui.py
├── utils/
│   └── file_handler.py
├── models/
│   └── gemini_api.py
├── agents/
│   ├── client_agent.py
│   ├── law_research_agent.py
│   ├── logic_analyzer.py
│   ├── legal_advisor.py
│   ├── opponent_lawyer.py
│   └── ai_judge.py
├── data/
│   └── sample_case.pdf
```

---

## 🛠️ Setup Instructions

### 1. Clone or Extract Folder

Unzip the folder and navigate into it:

```bash
unzip ai_powered_legal_council.zip
cd ai_powered_legal_council
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Gemini API Key

Export your Gemini API key (get it from https://makersuite.google.com/app/apikey):

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

On Windows (CMD):

```cmd
set GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 4. Run the Streamlit App

```bash
streamlit run main.py
```

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** – for interactive UI
- **Gemini LLM** – for AI reasoning & generation
- **PyMuPDF, Tesseract, Pillow** – for document parsing
- **Agentic AI** – for multi-role simulation (client, advisor, judge)

---


