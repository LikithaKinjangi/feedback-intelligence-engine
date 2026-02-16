# evaluation_engine.py
# Deterministic System Evaluation Layer


def evaluate_system(agent2_output):
    """
    Takes Agent 2 structured output and produces
    a human-readable system health summary.
    """

    category_distribution = agent2_output.get("category_distribution", {})
    priority_distribution = agent2_output.get("priority_distribution", {})
    high_priority_count = agent2_output.get("high_priority_count", 0)
    themes = agent2_output.get("detected_themes", [])

    total_themes = len(themes)
    total_problems = sum(len(theme.get("related_problems", [])) for theme in themes)

    # ---- Risk Level Assessment ----
    if high_priority_count >= 8:
        risk_level = "High"
    elif high_priority_count >= 4:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # ---- Theme Concentration ----
    if total_themes == 0:
        concentration = "No significant themes detected"
    elif total_themes == 1:
        concentration = "Highly concentrated issue cluster"
    elif total_themes <= 3:
        concentration = "Moderately concentrated themes"
    else:
        concentration = "Fragmented issue landscape"

    # ---- Signal Strength ----
    bug_count = category_distribution.get("Bug", 0)

    if bug_count >= 5 and high_priority_count >= 5:
        signal_strength = "Strong"
    elif high_priority_count >= 3:
        signal_strength = "Moderate"
    else:
        signal_strength = "Weak"

    summary = f"""
SYSTEM EVALUATION SUMMARY

Risk Level: {risk_level}
High Priority Issue Count: {high_priority_count}

Theme Count: {total_themes}
Total Problems Clustered: {total_problems}
Theme Concentration: {concentration}

Bug Volume: {bug_count}
Signal Strength: {signal_strength}

Interpretation:
- Risk level reflects urgency driven by high-priority issues.
- Theme concentration indicates whether issues are focused or spread across areas.
- Signal strength reflects severity based on bug dominance and priority load.
"""

    return summary


if __name__ == "__main__":

    # Example mock Agent 2 output for testing
    sample_agent2_output = {
        "category_distribution": {"Bug": 6, "Performance": 3, "Feature Request": 3, "Other": 5},
        "priority_distribution": {"High": 8, "Medium": 2, "Low": 9},
        "high_priority_count": 8,
        "detected_themes": [
            {"theme": "Upload Issues", "related_problems": ["Crash on upload", "Upload fails"]},
            {"theme": "Performance Issues", "related_problems": ["Slow dashboard"]},
            {"theme": "Authentication Issues", "related_problems": ["Session expires quickly"]}
        ]
    }

    result = evaluate_system(sample_agent2_output)

    print(result)