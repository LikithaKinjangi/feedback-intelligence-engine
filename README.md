# 🧠 Feedback Intelligence Engine
> AI-powered system that transforms raw user feedback into structured, prioritized product insights using a multi-agent architecture.

*This project is part of my journey as a Product enthusiast exploring AI systems, focused on understanding how LLMs can be orchestrated into reliable, structured product intelligence pipelines.*

---

## 📐 Architecture

View the interactive system architecture:

👉 [View Interactive Architecture Diagram](https://likithakinjangi.github.io/feedback-intelligence-engine/architecture-diagram.html)
## 📌 Project Overview

The Feedback Intelligence Engine takes unstructured user feedback and processes it through a multi-agent pipeline to generate:

1. **Structured feedback classification**
2. **Theme and pattern detection**
3. **Executive-style product insight memos**
4. **System-level risk evaluation**

The system runs fully locally using a local LLM (via Ollama), and includes both:

- **Manual Python orchestration** — learning version
- **LangGraph-based orchestration** — structured production-style flow
- **A Streamlit-based UI** — for real-time demonstration

---

## 💡 Why This Project Exists

As an individual exploring AI systems, I wanted to understand:

- How LLMs can return structured JSON outputs
- How to build tool-like agents around models
- How to orchestrate multi-agent pipelines
- How to translate raw feedback into product-level insights
- How control flow differs from business logic in AI systems

---

## 🏗️ System Architecture

### High-Level Flow

```
Raw Feedback
    → Agent 1 (Feedback Analyzer)
    → Agent 2 (Pattern Detector)
    → Agent 3 (Insight Generator)
    → Evaluation Layer
    → Product Intelligence Output
```

---

## 🤖 Agent Breakdown

### Agent 1 – Feedback Analyzer

Responsible for converting raw user text into structured format:

- Problem
- Sentiment
- Category
- Priority

**Key Learnings:**
- Enforcing JSON output from LLM
- Handling parsing failures
- Designing classification schema

---

### Agent 2 – Pattern Detector

Takes structured outputs from Agent 1 and:

- Groups similar problems
- Detects recurring themes
- Calculates category distribution
- Calculates priority distribution
- Counts high-priority items

**Key Learnings:**
- Batch analysis logic
- Theme clustering
- Product-level signal extraction

---

### Agent 3 – Insight Generator

Transforms pattern analysis into:

- Executive summary
- Risk areas
- Dominant themes
- Actionable recommendations

**Key Learnings:**
- Converting data signals into product memos
- Translating system metrics into business insights

---

### Evaluation Layer

Adds meta-analysis to the system:

- Risk level classification
- Signal strength assessment
- Theme concentration analysis
- Bug volume tracking

**Key Learnings:**
- System-level thinking
- Product health interpretation
- Risk framing

---

## ⚙️ Orchestration Approaches

### 1. Manual Python Orchestration *(Learning Reference)*

- Sequential execution
- Direct function calls
- Clear, readable logic

> **Purpose:** To deeply understand pipeline flow before introducing orchestration frameworks.

### 2. LangGraph Orchestration *(Primary Version)*

- Nodes represent agents
- Edges define execution flow
- State acts as shared memory
- Control flow separated from business logic

> **Purpose:** To model scalable multi-agent orchestration similar to production systems.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Local LLM Runtime | Ollama |
| Model | Llama3 |
| Orchestration | LangGraph |
| UI | Streamlit |
| Version Control | Git / GitHub |

---

## 🖥️ UI Layer

Built with **Streamlit** to:

- Accept real-time feedback input
- Run the full agent pipeline
- Display:
  - Pattern analysis
  - Insight memo
  - System evaluation
- Enable downloadable report *(optional enhancement)*

This allows the project to be demonstrated as a working AI product prototype.

---

## 📚 Key Learnings

Through this project, I learned:

- How LLMs can be used as structured tools
- Why JSON enforcement is critical for reliability
- How to design multi-agent systems
- Difference between orchestration and business logic
- How local LLM deployment differs from API-based usage
- How to debug environment and dependency conflicts
- How to think about AI systems from a product perspective

---

## 🔍 What This Is (and What It Is Not)

**This is:**
- A learning-driven AI product prototype
- A structured exploration of multi-agent design
- A product-oriented AI system experiment

**This is not:**
- A production-ready SaaS system
- A fine-tuned ML model
- A fully scalable infrastructure system

---

## 🚀 Future Enhancements

- [ ] Replace rule-based theme grouping with embedding-based clustering
- [ ] Add persistent storage for historical feedback
- [ ] Deploy UI to a cloud platform
- [ ] Add real-time analytics dashboard
- [ ] Add API layer for external integrations

---

## 🚀 Running the Project Locally

This project runs entirely on a local machine using a locally hosted LLM via Ollama.

### 1️⃣ Prerequisites

- Python 3.10+
- Ollama installed
- Llama 3 model pulled locally

**Install the model:**

```bash
ollama pull llama3
```

### 2️⃣ Clone the Repository

```bash
git clone https://github.com//feedback-intelligence-engine.git
cd feedback-intelligence-engine
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Start Ollama

```bash
ollama serve
```

### 6️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Then open: **http://localhost:8501**

---

> ⚠️ **Important Note**
> This system uses a local LLM via Ollama and does not depend on external APIs.
> It is intended for local experimentation and architectural learning.

---

## 🔮 Future Enhancements

- [ ] Replace rule-based theme grouping with embedding-based clustering
- [ ] Add persistent storage for historical feedback
- [ ] Deploy UI to a cloud platform
- [ ] Add real-time analytics dashboard
- [ ] Add API layer for external integrations

---
## 👤 Author

An individual exploring AI systems and multi-agent product design.
This repository reflects hands-on experimentation and structured learning in AI-powered product intelligence.
