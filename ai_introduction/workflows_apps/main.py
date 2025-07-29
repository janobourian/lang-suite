from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def generate_post(topic):
    response = client.responses.create(
        model="gpt-4.1",
        input = f"Create a social media post about {topic}"
    )
    return response.output_text

def main():
    print("Welcome to the AI Introduction Workflow App!")
    usr_input = input("Please enter the topic that you want to create a post: ")
    post = generate_post(usr_input)
    print(post)

if __name__ == "__main__":
    main()