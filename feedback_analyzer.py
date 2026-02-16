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
You are a strict product feedback analyzer.

Analyze the feedback and respond ONLY in valid JSON.
Do NOT include explanations.
Do NOT include markdown.
Do NOT include extra text.

Rules:
1. If the feedback describes a bug or issue → extract a clear "problem".
2. If the feedback is purely positive praise → set "problem" to "None".
3. If the feedback is a suggestion or feature request (e.g., "Please add dark mode") → set "problem" to "None".
4. "problem" must NEVER be empty or null. Use exactly "None" when there is no problem.
5. Output must be valid JSON with proper commas and double quotes.

Return JSON in this exact structure:

{{
  "problem": "string",
  "sentiment": "Positive/Neutral/Negative",
  "category": "Bug/Feature Request/UX Issue/Performance/Other",
  "priority": "High/Medium/Low"
}}

Feedback:
"{feedback_text}"
"""

    try:
        response = ollama.chat(               # Send prompt to LLM via Ollama
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    except Exception as e:
        print("⚠️ API call failed:", e)
        return {
            "problem": "API Failure",
            "sentiment": "Unknown",
            "category": "Other",
            "priority": "Low"
        }

    content = response["message"]["content"]

    # -------------------------
    # Robust JSON Extraction
    # -------------------------

    content = content.strip()

    # Attempt 1: Direct parse (best case)
    try:
        parsed = json.loads(content)
    except Exception:
        # Attempt 2: Extract JSON between first { and last }
        start = content.find("{")
        end = content.rfind("}")

        if start != -1 and end != -1:
            json_string = content[start:end + 1]
        else:
            json_string = content

        # Clean common model formatting issues
        json_string = json_string.replace("\n", " ")
        json_string = json_string.replace(", }", " }")
        json_string = json_string.replace(",}", "}")
        json_string = json_string.replace(": None", ': "None"')
        json_string = json_string.replace(": Positive", ': "Positive"')
        json_string = json_string.replace(": Neutral", ': "Neutral"')
        json_string = json_string.replace(": Negative", ': "Negative"')
        json_string = json_string.replace(": High", ': "High"')
        json_string = json_string.replace(": Medium", ': "Medium"')
        json_string = json_string.replace(": Low", ': "Low"')
        json_string = json_string.replace(": Bug", ': "Bug"')
        json_string = json_string.replace(": Feature Request", ': "Feature Request"')
        json_string = json_string.replace(": UX Issue", ': "UX Issue"')
        json_string = json_string.replace(": Performance", ': "Performance"')
        json_string = json_string.replace(": Other", ': "Other"')

        # Ensure closing brace exists
        if not json_string.strip().endswith("}"):
            json_string = json_string.strip() + "}"

        try:
            parsed = json.loads(json_string)
        except Exception:
            print("⚠️ JSON parsing failed.")
            print("Raw model output:")
            print(content)
            return {
                "problem": "Parsing Error",
                "sentiment": "Unknown",
                "category": "Other",
                "priority": "Low"
            }

    # -------------------------
    # Post-Processing Cleanup
    # -------------------------

    # Normalize invalid categorical values
    if parsed.get("category") == "None":
        parsed["category"] = "Other"

    if parsed.get("priority") == "None":
        parsed["priority"] = "Low"

    if parsed.get("sentiment") == "None":
        parsed["sentiment"] = "Neutral"

    if parsed.get("problem") in [None, "", "None"]:
        parsed["problem"] = "None"

    # Ensure "problem" field is never empty, null, or blank
    problem_value = parsed.get("problem")

    if problem_value is None or str(problem_value).strip() == "":
        parsed["problem"] = "None"

    return parsed


if __name__ == "__main__":

    test_feedbacks = [
        "Love the new UI, great job!",
        "App crashes when uploading PDF.",
        "The dashboard loads very slowly.",
        "Please add dark mode.",
        "This is useless.",
        "Sometimes login works, sometimes it doesn't.",
        "Performance improved a lot.",
        "I can't find settings anywhere.",
        "The new update broke everything.",
        "Good, but needs improvement."
    ]

    for feedback in test_feedbacks:
        print("\n-----------------------------")
        print("Feedback:", feedback)
        result = analyze_feedback(feedback)
        print(result)
