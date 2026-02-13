# Design Document  
## Feedback Intelligence Engine

## 1. Objective
The objective of this system is to convert unstructured user feedback into structured, machine-readable insights that can support product decision-making.

The system is designed using an agentic architecture that separates reasoning, tools, and orchestration logic.

## 2. Problem Statement
Product teams receive large volumes of raw user feedback such as:
1.App reviews  
2.Support tickets  
3.Survey responses  

Manually analyzing this feedback is:
1.Time-consuming  
2.Inconsistent  
3.Difficult to scale  
This system automates:
1.Sentiment detection  
2.Problem extraction  
3.Categorization  
4.Priority assignment  
The output is structured JSON for downstream processing.
## 3. System Architecture Overview
Raw User Feedback (Text)
↓
Agent 1 – Feedback Analyzer
↓
Structured JSON Output
↓
(Future) Agent 2 – Pattern Detector
↓
(Future) Agent 3 – Insight Generator
Current implementation focuses on Agent 1.

---

## 4. Architectural Layers
### 4.1 LLM Layer (Reasoning Engine)
- Model: Llama3 (via Ollama)
- Responsibility: Perform classification and structured reasoning
- Does not manage control flow
The LLM is treated as a reasoning component only.
### 4.2 Tool Layer (Modular Design)
The system follows a tool-based conceptual architecture.
#### 4.2.1 Sentiment Tool
Tool Name: `analyze_sentiment`
Input:
- feedback_text (string)
Output:
```json
{
  "sentiment": "Positive | Neutral | Negative"
}
```
Purpose:
1.Demonstrate tool abstraction
2.Enforce structured JSON output
3.Simulate function calling behavior.

## 4.2.2 Category Tool (Architectural Mapping)
Tool Name: categorize_feedback
Input:
feedback_text (string)
{
  "category": "Bug | Feature Request | UX Issue | Performance | Other"
}
Purpose:
- Classify feedback into predefined taxonomy
``(Currently implemented within Agent 1 prompt.)``
## 4.2.3 Priority Tool (Architectural Mapping)
Tool Name: assign_priority
Input:
- feedback_text (string)
Output:
```json
{
  "priority": "High | Medium | Low"
}
```
## 5. Agent 1 – Feedback Analyzer
Responsibilities:
	•	Construct structured prompts
	•	Invoke LLM via Ollama
	•	Enforce strict JSON schema output
	•	Parse response into Python dictionary
	•	Handle batch feedback inputs
Output Format:
```json
{
  "problem": "...",
  "sentiment": "...",
  "category": "...",
  "priority": "..."
}
```
### 6 Execution Flow
	1.	Raw feedback is provided as input.
	2.	Python constructs a structured prompt.
	3.	Prompt is sent to the LLM via ollama.chat().
	4.	The LLM performs reasoning and returns structured JSON.
	5.	Python parses JSON into a dictionary.
	6.	Structured output is stored for downstream use.
### 7. Design Principles
	1.Structured outputs instead of free text
	2.Clear separation between reasoning and control logic
	3.Modular tool abstraction
	4.Machine readable JSON output
	5.Model agnostic architecture
