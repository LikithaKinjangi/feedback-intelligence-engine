import ollama
import json


def analyze_sentiment(feedback_text):
    prompt = f"""
You are a sentiment analysis tool.

Analyze the sentiment of the following user feedback.

Respond ONLY in valid JSON format like this:

{{
  "sentiment": "Positive/Neutral/Negative"
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
    print("RAW MODEL OUTPUT:")
    print(content) 
    # Extract JSON block safely
    start = content.find("{")
    end = content.rfind("}") + 1
    json_string = content[start:end]

    return json.loads(json_string)
if __name__ == "__main__":
    sample_feedback = "The app crashes every time I try to upload a file."

    result = analyze_sentiment(sample_feedback)
    print(result)
    print(type(result))