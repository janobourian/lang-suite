from langgraph.graph import StateGraph, START, END, MessagesState
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def multiply(a:int|float, b:int|float) -> int|float:
    """Multiplies two numbers."""
    return a * b

llm_with_tools = llm.bind_tools([multiply])

def tool_calling_llm(state: MessagesState):
    return {'messages': [llm_with_tools.invoke(state['messages'])]}

class MessagesState(MessagesState):
    pass

builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_edge(START, "tool_calling_llm")
builder.add_edge("tool_calling_llm", END)
graph = builder.compile()