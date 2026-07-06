![AI Agent Yu helping a scientist](ai-scientist.png)

# AI Agent Yu

AI Agent Yu is a small coding assistant built during the Agentic AI masterclass by the appliedAI Institute.

The goal of this project is to learn how to build an **agentic coding assistant** from scratch using **Python** and **Pydantic AI**. 
The agent runs in the terminal and can help with simple coding tasks: understanding code, writing small functions, and explaining concepts.

## What this project demonstrates

- A conversational agent that keeps context across multiple turns.
- Tool-calling to work with files (read, write, search).
- Execution hooks for logging what the agent is doing.
- Dynamic control of reasoning effort (simple vs complex tasks).
- Loading extra “skills” from Markdown files to extend the assistant.

## Project structure

- `coding_assistant/main.py` – entry point, interactive loop for the assistant.
- `coding_assistant/utils.py` – helper functions (console, config, etc.).
- `coding_assistant/deps.py` – dependency container for the agent (e.g. console).
- `coding_assistant/capabilities/` – capabilities and tools:
  - `file_operations.py` – tools for reading/writing files.
  - `reasoning_effort.py` – adjusts reasoning level based on the prompt.
  - `skills.py` – loads and exposes external skills.

## How to run locally

1. Create and activate a Python environment (example with conda):
```bash
   conda create -n agentic-ai python=3.12 -y
   conda activate agentic-ai

    Install dependencies:

bash
python -m pip install "pydantic-ai[openai]" openai rich python-frontmatter

    Set your OpenAI-compatible API key (for example via environment variable):

bash
export OPENAI_API_KEY="sk-..."

    Run the assistant:

bash
python -m coding_assistant.main

You can now chat with the agent from your terminal.
Why this project exists

This repository is part of my THRIVE portfolio:
it shows that I can set up a local Python environment, use an LLM framework,
and design a simple but extensible agent that works on my own machine.
