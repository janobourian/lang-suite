from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import time

load_dotenv(override=True)
gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0)

def chat_gpt4o():
    message = input("Enter your message: ")
    start_time = time.perf_counter()
    result = gpt4o_chat.invoke(
        message
    )
    print(result.content)
    print(f"Time taken: {time.perf_counter() - start_time:.2f} seconds")

chat_gpt4o()