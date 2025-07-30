from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def generate_post(topic: str) -> str:
    prompt = f"""
You are an expert programmer and a business man specialized in creating successful tech enterprises on Silicon Valley.
You have a deep understanding of new business models and how technology can be used to create innovative solutions.
Your task is to create engaging, viral, and creative technology business ideas based on the given topic.
Your ideas should be concise, informative, and appealing to a wide audience.
The topic is:
<topic>
{topic}
</topic>

Here are some examples of successful tech business ideas:

<examples>
<example-1>
    <topic>
        Sustainable Agriculture
    </topic>
    <generated-business-idea>
        A platform that connects farmers with consumers, allowing for direct sales of organic produce while promoting sustainable farming practices.
    </generated-business-idea>
</example-1>
<example-2>
    <topic>
        Supply Chain Optimization
    </topic>
    <generated-business-idea>
        An AI-driven tool that helps businesses optimize their supply chain management by predicting demand and automating inventory management.
    </generated-business-idea>
</example-2>
<example-3>
    <topic>
        Remote Work Solutions
    </topic>
    <generated-business-idea>
        A comprehensive platform that offers tools for remote team collaboration, project management, and virtual office environments.
    </generated-business-idea>
</example-3>
</examples>

Do not use the examples above as a template, but rather as inspiration for your own unique ideas.
Do not use the tags in the examples above in your response.
Generate a new business idea based on the topic provided, ensuring it is original and not a direct copy of the examples.
The output should be a single, well-structured business idea that is ready to be presented or used as a starting point for further development.
Make sure to include the topic in your response.
    """
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    return response.output_text

def main() -> None:
    usr_input = input("Please enter the topic that you want to create a business idea: ")
    post = generate_post(usr_input)
    print(post)

if __name__ == "__main__":
    main()