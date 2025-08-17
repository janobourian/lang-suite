from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def get_single_request(input_text:str):
    response = client.responses.create(
        model="gpt-5",
        input=input_text
    )
    return response.output_text

def main():
    input_text = input("Please enter your input text: ")
    response = get_single_request(input_text)
    print(response)

if __name__ == "__main__":
    main()