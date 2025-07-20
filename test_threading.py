from langchain_openai import ChatOpenAI
import threading
import time

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def chat_gpt4o(message: str) -> None:
    """Function to chat with GPT-4o model."""
    response = llm.invoke(message)
    print(f"Response: {response.content}")


def main() -> None:
    start_time = time.perf_counter()
    messages = [
        "What is the capital of France?",
        "What is the largest mammal?",
        "Who wrote 'To Kill a Mockingbird'?",
        "What is the speed of light?",
        "What is the boiling point of water?",
        "What is the square root of 144?",
        "What is the chemical symbol for gold?",
        "What is the currency of Japan?",
        "What is the tallest mountain in the world?",
        "What is the main ingredient in guacamole?",
        "What is the capital of Australia?",
        "What is the largest planet in our solar system?",
        "What is the smallest country in the world?",
        "What is the longest river in the world?",
        "What is the main language spoken in Brazil?",
        "What is the largest desert in the world?",
        "What is the most spoken language in the world?",
        "What is the capital of Canada?",
        "What is the largest ocean on Earth?",
        "What is the main ingredient in sushi?",
        "What is the capital of Italy?"
    ]

    threads = []
    for message in messages:
        thread = threading.Thread(target=chat_gpt4o, args=(message,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f"All threads completed in {time.perf_counter() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()