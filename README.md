# AI Research Assistant Agent in Python 🤖📚

Welcome to the **AI Research Assistant** project! This repository contains a conversational AI agent designed to help you research topics, search the internet/Wikipedia, and automatically save the gathered insights to a local text file. 

The project is built using the **LangChain** framework, **Groq API** (powered by the fast `llama-3.3-70b-versatile` model), and python tools.

---

## 🌟 Features
- **Smart Tool Selection**: Automatically searches Wikipedia or the live internet (via DuckDuckGo) depending on the query.
- **Auto-Saving**: Saves research outputs to a local file (`Research_output.txt`) with timestamps.
- **Smart Filter for Casual Chitchat**: Politely declines non-research queries (like "tell me a joke" or "how are you?") in English/Hinglish, asking the user to focus on research topics.
- **Robust Exception Handling**: Prevents crashes by intercepting API or formatting issues and falling back gracefully.

---

## 📂 Project Structure

Here is a breakdown of the key files in the repository:

1. **[`main.py`](file:///e:/ai_agent_in_python/main.py)**: The entry point of the application. It initializes the Groq LLM, binds the tools, constructs the agent, and runs the input loop.
2. **[`agent.py`](file:///e:/ai_agent_in_python/agent.py)**: Contains the core `ResearchAgent` logic. It defines the system instructions (prompt template) and manages the `AgentExecutor` runtime.
3. **[`tools.py`](file:///e:/ai_agent_in_python/tools.py)**: Defines the custom Python functions (tools) that the LLM can invoke:
   - `internet_search_function`: Live web search via DuckDuckGo.
   - `wikipedia_search`: Wikipedia search for history and facts.
   - `save_to_txt`: Appends research details directly to a text file.
4. **[`requirments.txt`](file:///e:/ai_agent_in_python/requirments.txt)**: Contains the list of Python packages required to run this project.
5. **[`Research_output.txt`](file:///e:/ai_agent_in_python/Research_output.txt)**: The text file where the agent automatically logs your research results.

---

## 🚀 Setup & Installation

Follow these simple steps to run this project locally on your machine:

### 1. Set Up a Virtual Environment (Optional but Recommended)
Open your terminal in the project directory and run:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Activate the virtual environment (Mac/Linux)
source .venv/bin/activate
```

### 2. Install Dependencies
Install all the required Python libraries using the requirements file:
```bash
pip install -r requirments.txt
```

### 3. Configure Environment Variables
Create a file named `.env` in the root of the project and add your Groq API Key:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

---

## 💻 How to Use

To start the agent, run the following command:
```bash
python main.py
```

### Examples of how the agent behaves:

#### Example 1: Factual/Research Query
```text
Put your query here: what is the capital of france ?
Executing query...
*Agent calls wikipedia_search*
*Agent calls save_to_txt*

--- Agent Final Output ---
The capital of France is Paris. (And it gets saved to Research_output.txt)
```

#### Example 2: Casual Conversation (Non-Research)
```text
Put your query here: how are you ?
Executing query...

--- Agent Final Output ---
Namaste, I'm doing well, thank you for asking. However, I'm a research assistant designed to help with research papers. Please ask a research-oriented question.
```

---

## 🛠️ Technology Stack
- **Framework**: LangChain (for agent orchestration)
- **LLM**: Groq ChatGroq (Llama-3.3-70b)
- **Libraries**:
  - `duckduckgo-search` (Live Web Results)
  - `wikipedia` (Wikipedia API wrapper)
  - `python-dotenv` (Environment variables management)
  - `pydantic` (Data schema validation)