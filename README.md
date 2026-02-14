# Feedback Intelligence Engine

AI-powered spwd
ystem that transforms raw user feedback into structured, prioritized product insights.

---

## Day 1 Progress

### Environment Setup
- Python installed
- Git initialized
- Ollama installed
- Llama3 model downloaded

### First Model Call
- Successfully connected Python to local LLM (Ollama)
- Executed working model call via `ollama.chat()`

### Files Created
- python_basics.py
- local_llm_test.py
- feedback_analyzer.py
- .gitignore
- README.md

---
## Day 2 Progress

### Sentiment Analyzer Tool
- Created standalone `sentiment_analyzer.py`
- Returns structured JSON output
- Simulates function-calling behavior
- Validated with sample feedback
## Current Status
Agent 1 (Feedback Analyzer) under development.
## Day 4 Progress – LangGraph Foundation
### LangGraph Study
Studied the core concepts of LangGraph orchestration:
- **Node**: A unit of work that takes the current state as input, performs processing, and returns an updated state.
- **Edge**: Defines execution flow between nodes (linear or conditional routing).
- **State**: A structured dictionary that acts as shared context passed between nodes during a single graph execution.
- **State Management**: Ensuring each node updates only its relevant fields without overwriting the entire state.
### Prototype Implementation
- Built a "Hello World" LangGraph example.
- Implemented linear node flow.
- Implemented conditional routing between nodes.
- Verified state propagation across nodes.
### Key Learning
LangGraph separates:
- Business logic (inside nodes)
- Control flow (defined by graph structure)
This enables modular, scalable multi-agent orchestration.