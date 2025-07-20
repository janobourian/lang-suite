from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, START, StateGraph
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition

def multiply(a: int | float, b: int | float) -> int | float:
    """Multiplies two numbers."""
    return a * b

def add(a: int | float, b: int | float) -> int | float:
    """Adds two numbers."""
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts two numbers."""
    return a - b

def divide(a: int | float, b: int | float) -> int | float:
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

tools = [multiply, add, subtract, divide]

llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

# Node
def assistant_node(state: MessagesState) -> MessagesState:
    return {"messages": llm_with_tools.invoke([sys_msg]+ state["messages"])}

# Graph
builder = StateGraph(MessagesState)

# Node
builder.add_node("assistant", assistant_node)
builder.add_node("tools", ToolNode(tools))

# Edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

# Define the graph
graph = builder.compile()