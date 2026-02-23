import ollama


def generate_insights(agent2_output):
    """
    Takes structured analytics from Agent 2
    and generates a structured executive product memo.
    """

    prompt = f"""
You are a senior Product Strategy Analyst.

Based on the following analytics summary, generate a structured product memo.

Analytics Input:
{agent2_output}
STRICT RULES:
- You MUST NOT calculate totals, ratios, percentages, or derived statistics.
- You MUST NOT infer overall issue counts.
- Only reference values explicitly shown in the Analytics Input.
- You may reference "high_priority_count" directly if needed.
- Do NOT combine category counts into totals.
- Do NOT create new numerical statements.
- Avoid speculative language.

Your response MUST follow this structure:

Executive Summary:
(Brief 3-4 sentence overview of product health)

Key Risk Areas:
(List major risk signals based on high priority counts or repeated themes)

Dominant Themes:
(List major themes detected and what they indicate)

Recommended Actions:
(Provide prioritized, actionable product recommendations)

Keep it concise, strategic, and suitable for leadership review.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    # Example test input (mock Agent 2 output)
    sample_agent2_output = {
        "category_distribution": {"Bug": 6, "Performance": 3, "Feature Request": 3, "Other": 5},
        "priority_distribution": {"High": 8, "Medium": 2, "Low": 9},
        "high_priority_count": 8,
        "detected_themes": [
            {"theme": "Upload Issues", "related_problems": ["App crashes on upload", "Upload fails for large files"]},
            {"theme": "Performance Issues", "related_problems": ["Dashboard loads slowly"]},
            {"theme": "Authentication Issues", "related_problems": ["Session expires too quickly"]}
        ]
    }

    result = generate_insights(sample_agent2_output)

    print("\n=== PRODUCT INSIGHT MEMO ===\n")
    print(result)
