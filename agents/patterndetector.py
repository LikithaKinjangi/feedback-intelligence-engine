# pattern_detector.py
# Agent 2: Pattern Detector
# Purpose:
# Takes structured outputs from Agent 1 and:
# - Aggregates category distribution
# - Aggregates priority distribution
# - Counts high priority issues
# - Collects valid problem statements

import ollama
import json
from collections import Counter


def detect_patterns(agent1_results):
    """
    agent1_results: list of dictionaries from Agent 1

    Returns:
        dict containing deterministic aggregation results
    """

    # Validate input
    if not isinstance(agent1_results, list):
        raise ValueError("Input must be a list of Agent 1 results")

    category_counter = Counter()
    priority_counter = Counter()
    high_priority_count = 0
    problems = []

    for item in agent1_results:
        category = item.get("category")
        priority = item.get("priority")
        problem = item.get("problem")

        if category:
            category_counter[category] += 1

        if priority:
            priority_counter[priority] += 1
            if priority == "High":
                high_priority_count += 1

        if problem and problem != "None":
            problems.append(problem)
    themes = detect_semantic_themes(problems) if problems else []
    return {
        "category_distribution": dict(category_counter),
        "priority_distribution": dict(priority_counter),
        "high_priority_count": high_priority_count,
        "detected_themes": themes
    }
 
def detect_semantic_themes(problems):
    """
    Uses LLM to group similar problems into semantic themes.
    Returns structured JSON themes list.
    """

    if not problems:
        return []

    prompt = f"""
You are a precise product issue clustering engine.

Your task:
Group the following problems into DISTINCT and SPECIFIC themes.

Rules:
1. You MUST include ALL problems in the output. No problem should be omitted.
2. If a problem does not belong to an existing theme, create a NEW specific theme for it.
3. Do NOT create overly broad themes.
4. Each theme name MUST be a clear technical noun phrase and MUST end with "Issues".
   Example: "Upload Issues", "Authentication Issues", "Performance Issues".
5. Even if only ONE problem belongs to a theme, it must still appear as its own theme.
6. Do not merge unrelated issues.

Return ONLY valid JSON in this format:

{{
  "themes": [
    {{
      "theme": "Specific Theme Name Issues",
      "related_problems": ["problem1", "problem2"]
    }}
  ]
}}

Problems:
{problems}
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response["message"]["content"].strip()

        try:
            parsed = json.loads(content)
            return parsed.get("themes", [])
        except Exception:
            start = content.find("{")
            end = content.rfind("}")

            if start != -1 and end != -1:
                json_string = content[start:end + 1]
            else:
                return []

            json_string = json_string.replace("\n", " ")
            json_string = json_string.replace(", }", " }")
            json_string = json_string.replace(",}", "}")

            if not json_string.strip().endswith("}"):
                json_string += "}"

            try:
                parsed = json.loads(json_string)
                return parsed.get("themes", [])
            except Exception:
                return []

    except Exception:
        return []
if __name__ == "__main__":
    sample_input = [
        {"problem": "App crashes on upload", "sentiment": "Negative", "category": "Bug", "priority": "High"},
        {"problem": "Upload fails for large file", "sentiment": "Negative", "category": "Bug", "priority": "High"},
        {"problem": "None", "sentiment": "Positive", "category": "Other", "priority": "Low"},
        {"problem": "Dashboard loads slowly", "sentiment": "Negative", "category": "Performance", "priority": "Medium"},
        {"problem": "None", "sentiment": "Positive", "category": "Feature Request", "priority": "Low"}
    ]

    result = detect_patterns(sample_input)
    print(result)