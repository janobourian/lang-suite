from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
import time

init_time = time.perf_counter()

messages = [AIMessage(content="Hola, ¿cómo estás?", name="dardo")]
messages.append(HumanMessage(content="Estoy bien, gracias. ¿Y tú?", name="franco"))
messages.append(AIMessage(content="Muy bien, gracias por preguntar.", name="dardo"))
messages.append(HumanMessage(content="¿Cuánto es 2 por 3?", name="franco"))

for m in messages:
    print(f"{m.name}: {m.content}")

llm = ChatOpenAI(model="gpt-4o")

def multiply(a: int | float, b: int | float) -> int | float:
    print(f"Multiplying {a} by {b}")
    return a * b

llm_with_tools = llm.bind_tools([multiply])

result = llm_with_tools.invoke(messages)
print(f"LLM response: {result.additional_kwargs.get('tool_calls', [])}")

print(f"Time taken: {time.perf_counter() - init_time:.2f} seconds")

## Messages as State

class MessageState(MessagesState):
    pass

# Node
def tool_calling_llm(state: MessageState):
    return {"messages": [llm_with_tools.invoke(state['messages'])]}

# Build a graph
builder = StateGraph(MessageState)
builder.add_node("tool_calling_llm", tool_calling_llm)

# Logic
builder.add_edge(START, "tool_calling_llm")
builder.add_edge("tool_calling_llm", END)
graph = builder.compile()