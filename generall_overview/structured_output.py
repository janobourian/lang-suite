from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from uuid import uuid4

load_dotenv()
client = OpenAI()

class UserInfo(BaseModel):
    id: uuid4
    name: str
    email: str
    age: int

response = client.responses.parse(
    model="gpt-5",
    reasoning={"effort": "low"},
    instructions="You are a helpful assistant that provides fake and random information to fulfill user databases",
    input="Create a random user information for a mexican user",
    text_format=UserInfo
)

print(response.output_parsed.model_dump())