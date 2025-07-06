from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from langgraph.graph import MessagesState

class MessagesState(TypedDict):
    messages: list[AnyMessage]

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

class MessagesState(MessagesState):
    pass