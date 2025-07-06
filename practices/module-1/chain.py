from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import time

llm = ChatOpenAI(model="gpt-4o", temperature=0)

messages = [AIMessage(content="So you said you were researching ocean mammals?", name="Model")]
messages.append(HumanMessage(content="Yes, that's right! I was looking into dolphins and whales.", name="Maxine"))
messages.append(AIMessage(content="Great, what would you like to learn about", name="Model"))
messages.append(HumanMessage(content="I want to learn about the best place to see Orcas in Mexico.", name="Maxine"))

for m in messages:
    print(f"{m.name}: {m.content}")

start_time = time.perf_counter()
print("Starting chat execution...")
result = llm.invoke(messages)
print(f"Chat execution completed in {time.perf_counter() - start_time:.6f} seconds")
print(f"Model: {result.content}")
print(f"Result: {result}")
print(f"Result type: {type(result)}")
print(f"Result metadata: {result.response_metadata}")

def multiply(a:int|float, b:int|float) -> int|float:
    """Multiplies two numbers."""
    return a * b

llm_with_tools = llm.bind_tools([multiply])

tool_call = llm_with_tools.invoke([HumanMessage(content="What is 3 times 4?", name="Lance")])
print(f"Tool call result: {tool_call}")
print(tool_call.additional_kwargs['tool_calls'])