# Python for AI — Learning Journey

This repo documents my hands-on path into Python, with the long-term goal of building real AI-powered tools (chatbots, content generators, and automation) for businesses and clients.

I'm a beginner, and I've organized this repo into two clear sections so it's obvious what I built myself versus what I followed along with while learning.

## 📁 `projects/` — Built and debugged by me

These are projects where I wrote the logic myself and worked through real bugs and errors independently (with guidance, not copy-pasted solutions).

### `calculator.py`
A command-line calculator. Covers:
- Conditionals (`if`/`elif`/`else`)
- Error handling with `try`/`except` (division by zero)
- Input validation (re-prompts on invalid operator)
- Looping until the user chooses to quit

### `todo.py`
A command-line to-do list manager. Covers:
- Lists and list methods (`.append()`, `.pop()`)
- Menu-driven loops
- Error handling for invalid task numbers (`IndexError`)

### `gemini_chatbot.py`
A working, business-scoped AI chatbot built using Google's Gemini API (`google-genai` SDK). Covers:
- Securely loading API keys via environment variables
- Real API calls to an LLM with conversation memory
- A custom **system prompt** that scopes the bot to a specific business persona (demoed here as a bakery assistant) — the core technique behind sellable "AI chatbot for your business" tools
- Graceful error handling for API/server issues

### `pandas_practice.py`
Built from scratch (not following the course) to actually understand `pandas` fundamentals after realizing I could follow instructor code but not yet write my own:
- Creating and reading DataFrames
- Column-wide operations without loops
- Filtering rows by condition (`df[df["column"] == value]`)

## 📁 `learning-exercises/` — Course-guided exercises

These were built while following along with a Python course. I understand the concepts at a guided level but want to be transparent that I didn't write this logic independently (yet).

- **`shopping_cart.py`** — functions, dictionaries, and loops (calculates a cart total)
- **`get_data.py`** — pulls live weather data via API, processes with `pandas`, visualizes with `matplotlib`
- **`sales-analysis/`** — sales data analysis using `pandas` (`analyzer.py`, `helpers.py`)

## 🛠️ Tech Used
Python · pandas · matplotlib · requests · Google Gemini API (`google-genai`)

## 🎯 Why this repo exists
I'm learning Python with the specific goal of building AI tools (chatbots, content automation) that solve real problems for small businesses. The `projects/` folder is my actual portfolio — proof of what I can build and debug independently. More will be added as I go.