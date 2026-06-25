# Python for AI — Learning Journey

This repo documents my hands-on path into Python, with the long-term goal of building real AI-powered tools (chatbots, content generators, and automation) for businesses and clients.

I'm a beginner, and these projects were built and debugged step by step — some bugs, fixes, and messy bits are part of the learning process, not hidden.

## 📁 Projects

### `calculator.py`
A command-line calculator. Covers:
- Basic arithmetic with conditionals (`if`/`elif`/`else`)
- Error handling with `try`/`except` (e.g. division by zero)
- Input validation (re-prompts on invalid operator)
- Looping until the user chooses to quit

### `todo.py`
A command-line to-do list manager. Covers:
- Lists and list methods (`.append()`, `.pop()`)
- Menu-driven loops
- Error handling for invalid task numbers (`IndexError`)

### `gemini_chatbot.py`
A working AI chatbot built using Google's Gemini API (`google-genai` SDK). Covers:
- Securely loading API keys via environment variables (never hardcoded)
- Making real API calls to an LLM
- Maintaining conversation memory using a chat session

### `shopping_cart.py`
An early exercise using functions, dictionaries, and loops — calculates a shopping cart total from a list of items.

### `get_data.py`
Pulls live weather data for Rawalpindi from the Open-Meteo API, processes it with `pandas`, visualizes it with `matplotlib`, and saves the result to CSV.
- Output: `weather_chart.png`, `data/rawalpindi_weather.csv`

### `sales-analysis/`
A small sales data analysis tool.
- `analyzer.py` — reads sales data from CSV, calculates totals per item and a grand total
- `helpers.py` — helper functions for calculations and currency formatting
- `data/` — input CSV data
- `output/` — generated results

## 🛠️ Tech Used
Python · pandas · matplotlib · requests · Google Gemini API (`google-genai`)

## 🎯 Why this repo exists
I'm learning Python with the specific goal of building AI tools (chatbots, content automation) that solve real problems for small businesses. This repo is my visible progress log — more projects will be added as I go.
