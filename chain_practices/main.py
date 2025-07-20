from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

summary_template = """Giving the next number {number} tell me if it is a prime number or not.
If it is a prime number, return "Yes, it is a prime number."
If it is not a prime number, return nothing.
"""

summary_prompt = PromptTemplate(
    input_variables=["number"],
    template=summary_template)

llm = ChatOpenAI(model="gpt-4o", temperature=0)

chain = summary_prompt | llm

result = chain.invoke({"number": 37})
print(f"Result: {result.content}")
