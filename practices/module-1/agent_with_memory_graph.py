from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver

def multiply(a: int | float, b: int | float) -> int | float:
    """Multiplies two numbers."""
    return a * b

def divide(a: int | float, b: int | float) -> int | float:
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def add(a: int | float, b: int | float) -> int | float:
    """Adds two numbers."""
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts two numbers."""
    return a - b

tools = [multiply, divide, add, subtract]
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Graph
builder = StateGraph(MessagesState)

# Nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

# Copile the graph
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

# Specify a thread
config = {"configurable": {"thread_id": "1"}}

messages = [HumanMessage(content="What is 2 * 3?"),]
messages = graph.invoke({'messages':messages}, config)
for message in messages["messages"]:
    print(message.content)

messages = [HumanMessage(content="Add 5 by that"),]
messages = graph.invoke({'messages':messages}, config)
for message in messages["messages"]:
    print(message.content)