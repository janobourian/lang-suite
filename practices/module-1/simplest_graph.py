import random
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    graph_state: str

def node_1(state: State):
    print('--- Node 1 ---')
    return {'graph_state': state['graph_state'] +  "I am "}

def node_2(state:State):
    print('--- Node 2 ---')
    return {'graph_state': state['graph_state'] + "happy!"}

def node_3(state:State):
    print('--- Node 3 ---')
    return {'graph_state': state['graph_state'] + "sad!"}

def decide_mood(_:State) -> Literal["node_2", "node_3"]:
    print('--- Deciding mood ---')
    return "node_2" if random.random() < 0.5 else "node_3"

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Add
graph = builder.compile()

result = graph.invoke({"graph_state": "Hi, this is Maxine. "})

print(result)