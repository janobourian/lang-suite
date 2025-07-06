from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import time

load_dotenv(override=True)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def multiply(a:int|float, b:int|float) -> str:
    """Multiplies two numbers."""
    return f"The result of {a} time {b} is: {a * b}"

llm_with_tools = llm.bind_tools([multiply])
tool_call = llm_with_tools.invoke([HumanMessage(content="What is 2.3 times 3.45?", name="Maxine")])
print(f"dir(tool_call): {dir(tool_call)}")
print(f"Tool call: {tool_call}")
print(f"Tool result: {tool_call.content}")
print(f"Tool calls: {tool_call.tool_calls}")

tool_call = llm_with_tools.invoke([HumanMessage(content="What is 2.1 plus 15.1?", name="Maxine")])
print(f"dir(tool_call): {dir(tool_call)}")
print(f"Tool call: {tool_call}")
print(f"Tool result: {tool_call.content}")
print(f"Tool calls: {tool_call.tool_calls}")