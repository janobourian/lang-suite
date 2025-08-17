from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "high"},
    instructions="Generate a detailed explanation like a professor would.",
    input="What is the meaning of life?"
)

print(response.output_text)