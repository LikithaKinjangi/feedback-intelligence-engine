from typing import TypedDict
from langgraph.graph import StateGraph, END
# 1️ Define the structure of our shared state
class MyState(TypedDict):
    message: str
# 2️ Define a node (unit of work)
def hello_node(state: MyState) -> MyState:
    print("Inside Node")
    state["message"] += " World"
    return state

# New node: exclaim_node
def exclaim_node(state: MyState) -> MyState:
    print("Inside Exclaim Node")
    state["message"] += "!!!"
    return state
# 3️ Create the graph
builder = StateGraph(MyState)
# 4️ Add node to graph
builder.add_node("hello", hello_node)
builder.add_node("exclaim", exclaim_node)
# 5️ Define entry point
builder.set_entry_point("hello")
# 6️ Define where to go after node runs
builder.add_edge("hello", "exclaim")
builder.add_edge("exclaim", END)
# 7️ Compile the graph
graph = builder.compile()
# 8 Run the graph
initial_state = {"message": "Hello"}
result = graph.invoke(initial_state)
print("Final State:", result)

# -----------------------------
# Conditional Routing Example
# -----------------------------

print("\n--- Conditional Graph Example ---")

# Extend state for routing
class ConditionalState(TypedDict):
    message: str
    route: str

def conditional_hello_node(state: ConditionalState) -> ConditionalState:
    print("Inside Conditional Hello Node")
    state["message"] += " World"

    if len(state["message"]) > 10:
        state["route"] = "long"
    else:
        state["route"] = "short"

    return state

def long_node(state: ConditionalState) -> ConditionalState:
    print("Inside Long Node")
    state["message"] += "!!!"
    return state

# Build conditional graph
conditional_builder = StateGraph(ConditionalState)

conditional_builder.add_node("hello", conditional_hello_node)
conditional_builder.add_node("long", long_node)

conditional_builder.set_entry_point("hello")

def router(state: ConditionalState):
    return state["route"]

conditional_builder.add_conditional_edges(
    "hello",
    router,
    {
        "long": "long",
        "short": END
    }
)

conditional_builder.add_edge("long", END)

conditional_graph = conditional_builder.compile()

initial_state_2 = {"message": "Hi", "route": ""}
result_2 = conditional_graph.invoke(initial_state_2)

print("Final Conditional State:", result_2)