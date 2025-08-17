from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
client = OpenAI()

class UserData(BaseModel):
    name: str
    age: int
    email: str
    address: str

def get_openai_response(prompt: str) -> UserData:
    response = client.responses.parse(
        model="gpt-4.1",
        input=prompt,
        text_format=UserData
    )
    return response.output_parsed

def main() -> None:
    prompt = "Give me a random user data from Mexico City"
    response = get_openai_response(prompt)
    print(f"Response: {response.model_dump()}")

if __name__ == "__main__":
    main()