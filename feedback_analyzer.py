#feedback_analyzer.py

#Agent 1: Feedback Analyzer
#Purpose:
#Transforms raw user feedback into structured JSON insights including:
#- Problem extraction
#- Sentiment classification
#- Category classification
#- Priority assignment
#This file acts as the orchestration layer between:
#- Python control logic
#- LLM reasoning (via Ollama)
import ollama
import json


def analyze_feedback(feedback_text):
    """
    Analyze user feedback using LLM reasoning.

    Parameters:
        feedback_text (str): Raw user feedback text.

    Returns:
        dict: Structured dictionary containing:
              - problem
              - sentiment
              - category
              - priority
    """
# Construct structured prompt to enforce JSON output
    prompt = f"""              
You are a product feedback analyzer.

Analyze the feedback and respond ONLY in valid JSON format like this:

{{
  "problem": "...",
  "sentiment": "Positive/Neutral/Negative",
  "category": "Bug/Feature Request/UX Issue/Performance/Other",
  "priority": "High/Medium/Low"
}}

Feedback:
"{feedback_text}"
"""

    response = ollama.chat(               # Send prompt to LLM via Ollama
        model="llama3", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response["message"]["content"]

    # Extract JSON block safely
    start = content.find("{")
    end = content.rfind("}") + 1
    json_string = content[start:end]

    return json.loads(json_string)


if __name__ == "__main__":
    feedback_list = [
        "The app crashes every time I upload a file.",
        "Dark mode would be really helpful at night.",
        "Login takes too long sometimes.",
        "The new dashboard design looks great!",
        "Notifications are not working properly."
    ]

    analyzed_results = []

    for feedback in feedback_list:
        result = analyze_feedback(feedback)
        analyzed_results.append(result)

    print(analyzed_results)
    print(type(analyzed_results))