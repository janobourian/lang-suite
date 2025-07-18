from typing_extensions import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
import random
import time

def random_time():
    time.sleep(random.uniform(0.1, 0.7))

# State
class State(TypedDict):
    graph_state: str

# Nodes
def node_1(state: State):
    print('--- Node 1 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_1'}

def node_2(state: State):
    print('--- Node 2 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_2'}

def node_3(state: State):
    print('--- Node 3 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_3'}

def node_4(state: State):
    print('--- Node 4 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_4'}

def node_5(state: State):
    print('--- Node 5 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_5'}

def node_6(state: State):
    print('--- Node 6 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_6'}

def node_7(state: State):
    print('--- Node 7 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_7'}

def node_8(state: State):
    print('--- Node 8 ---')
    print("Current state:", state['graph_state'])
    return {'graph_state': 'node_8'}

def first_decision(_: State) -> Literal["node_2", "node_3"]:
    print('--- First decision ---')
    return "node_2" if random.random() < 0.5 else "node_3"

def second_decision(_: State) -> Literal["node_5", "node_6"]:
    print('--- Second decision ---')
    return "node_5" if random.random() < 0.5 else "node_6"

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_node("node_4", node_4)
builder.add_node("node_5", node_5)
builder.add_node("node_6", node_6)
builder.add_node("node_7", node_7)
builder.add_node("node_8", node_8)

# Logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", first_decision)
builder.add_edge("node_2", "node_4")
builder.add_edge("node_3", "node_4")
builder.add_conditional_edges("node_4", second_decision)
builder.add_edge("node_6", "node_7")
builder.add_edge("node_5", "node_8")
builder.add_edge("node_7", END)
builder.add_edge("node_8", END)

# Add
graph = builder.compile()

# View
result = graph.invoke({"graph_state": "Starting state. "})

print(result)