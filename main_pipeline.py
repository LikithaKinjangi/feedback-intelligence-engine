# main_pipeline.py
# End-to-End Integration: Agent 1 → Agent 2

from feedback_analyzer import analyze_feedback
from patterndetector import detect_patterns
from insight_generator import generate_insights
from evaluation_engine import evaluate_system


def run_pipeline(raw_feedback_list):
    structured_results = []

    print("\n--- Running Agent 1 (Feedback Analyzer) ---")

    for feedback in raw_feedback_list:
        result = analyze_feedback(feedback)
        structured_results.append(result)
        print("Processed:", feedback)

    print("\n--- Running Agent 2 (Pattern Detector) ---")

    pattern_output = detect_patterns(structured_results)

    print("\n--- Running Agent 3 (Insight Generator) ---")
    insight_output = generate_insights(pattern_output)

    print("\n--- Running Evaluation Layer ---")
    evaluation_output = evaluate_system(pattern_output)

    return {
        "pattern_analysis": pattern_output,
        "insight_memo": insight_output,
        "system_evaluation": evaluation_output
    }


if __name__ == "__main__":

    sample_feedback = [
        "App crashes when uploading images.",
        "Upload fails for large PDF files.",
        "File upload not working properly.",
        "Dashboard takes too long to load.",
        "The app feels very slow after update.",
        "Reports page is lagging badly.",
        "Login session expires too quickly.",
        "Cannot log in with correct password.",
        "OTP verification fails sometimes.",
        "Please add dark mode.",
        "Would love an export to Excel feature.",
        "Add multi-language support.",
        "Love the new UI design!",
        "Great job on the latest update.",
        "Good but needs improvement.",
        "It works fine most of the time.",
        "",
        "???",
        "App good but sometimes bad."
    ]

    final_result = run_pipeline(sample_feedback)

    print("\n=== FINAL PATTERN ANALYSIS ===")
    print(final_result["pattern_analysis"])

    print("\n=== PRODUCT INSIGHT MEMO ===")
    print(final_result["insight_memo"])

    print("\n=== SYSTEM EVALUATION SUMMARY ===")
    print(final_result["system_evaluation"])
# main_pipeline.py
# LangGraph Orchestrated Pipeline (Primary)
# Manual Python Orchestration kept for learning reference

from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph

from feedback_analyzer import analyze_feedback
from patterndetector import detect_patterns
from insight_generator import generate_insights
from evaluation_engine import evaluate_system


# =========================================================
# =============== LEARNING VERSION (MANUAL) ==============
# =========================================================

def run_manual_pipeline(raw_feedback_list):
    """
    Manual orchestration using plain Python.
    Kept for learning curve reference.
    """

    structured_results = []

    for feedback in raw_feedback_list:
        result = analyze_feedback(feedback)
        structured_results.append(result)

    pattern_output = detect_patterns(structured_results)
    insight_output = generate_insights(pattern_output)
    evaluation_output = evaluate_system(pattern_output)

    return {
        "pattern_analysis": pattern_output,
        "insight_memo": insight_output,
        "system_evaluation": evaluation_output
    }


# =========================================================
# =============== LANGGRAPH VERSION (PRIMARY) ============
# =========================================================

class PipelineState(TypedDict):
    raw_feedback: List[str]
    structured_results: List[Dict]
    pattern_analysis: Dict
    insight_memo: str
    system_evaluation: str


def agent1_node(state: PipelineState):
    structured = []
    for feedback in state["raw_feedback"]:
        result = analyze_feedback(feedback)
        structured.append(result)

    return {"structured_results": structured}


def agent2_node(state: PipelineState):
    pattern_output = detect_patterns(state["structured_results"])
    return {"pattern_analysis": pattern_output}


def agent3_node(state: PipelineState):
    insight_output = generate_insights(state["pattern_analysis"])
    return {"insight_memo": insight_output}


def evaluation_node(state: PipelineState):
    evaluation_output = evaluate_system(state["pattern_analysis"])
    return {"system_evaluation": evaluation_output}


def build_langgraph_pipeline():
    workflow = StateGraph(PipelineState)

    workflow.add_node("Agent1", agent1_node)
    workflow.add_node("Agent2", agent2_node)
    workflow.add_node("Agent3", agent3_node)
    workflow.add_node("Evaluation", evaluation_node)

    workflow.set_entry_point("Agent1")
    workflow.add_edge("Agent1", "Agent2")
    workflow.add_edge("Agent2", "Agent3")
    workflow.add_edge("Agent3", "Evaluation")

    return workflow.compile()


# =========================================================
# ========================= RUN ===========================
# =========================================================

if __name__ == "__main__":

    sample_feedback = [
        "App crashes when uploading images.",
        "Upload fails for large PDF files.",
        "File upload not working properly.",
        "Dashboard takes too long to load.",
        "The app feels very slow after update.",
        "Reports page is lagging badly.",
        "Login session expires too quickly.",
        "Cannot log in with correct password.",
        "OTP verification fails sometimes.",
        "Please add dark mode.",
        "Would love an export to Excel feature.",
        "Add multi-language support.",
        "Love the new UI design!",
        "Great job on the latest update.",
        "Good but needs improvement.",
        "It works fine most of the time.",
        "",
        "???",
        "App good but sometimes bad."
    ]

    print("\n=== Running LangGraph Orchestrated Pipeline ===")

    graph = build_langgraph_pipeline()

    final_state = graph.invoke({
        "raw_feedback": sample_feedback,
        "structured_results": [],
        "pattern_analysis": {},
        "insight_memo": "",
        "system_evaluation": ""
    })

    print("\n=== FINAL PATTERN ANALYSIS ===")
    print(final_state["pattern_analysis"])

    print("\n=== PRODUCT INSIGHT MEMO ===")
    print(final_state["insight_memo"])

    print("\n=== SYSTEM EVALUATION SUMMARY ===")
    print(final_state["system_evaluation"])