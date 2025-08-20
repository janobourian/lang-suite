from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

file = client.files.create(
    file=open("./generall_overview/cv.pdf", "rb"),
    purpose="user_data"
)

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "high"},
    input=[
        {
            'role': 'user',
            'content': [
                {
                    'type': 'input_file',
                    'file_id': file.id,
                },
                {
                    'type': 'input_text',
                    'text': 'Analyze the CV and provide a summary of the skills and experiences listed.'
                }
            ]
        }
    ]
)

print(response.output_text)