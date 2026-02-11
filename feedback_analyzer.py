import ollama
import json


def analyze_feedback(feedback_text):
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

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response["message"]["content"]
    return json.loads(content)


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