from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv(override=True)

gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0)
gpt35_chat = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Long way
msg = HumanMessage(
    content="Hello, give me a list of the twenty fastest programming languajes, sorted by the fastest ",
    name="Lance",
)
messages = [msg]
result = gpt4o_chat.invoke(messages)
print(result.content)

# Short way
result = gpt4o_chat.invoke(
    "Hello, give me a list of the twenty fastest web framerowks to build applications servers"
)
print(result.content)

# Tavily Search
tavily_search = TavilySearchResults(max_results=3)
search_docs = tavily_search.invoke("What is Python decorator?")
print(search_docs)
