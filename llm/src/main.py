from typing import Annotated, TypedDict

from fastapi import FastAPI
# from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0"
)

llm_model = ChatBedrock(
    model_id='anthropic.claude-3-haiku-20240307-v1:0',
    model_kwargs=dict(temperature=0.5)
)

add_routes(
    app,
    # ChatOpenAI(model="gpt-3.5-turbo"),
    llm_model,
    path='/anthropic'
)


@tool
def weather(query: str):
    # return f"Today's weather is sunny in {query}."
    return "晴れのち雨です"


tools = [weather]
llm_model = llm_model.bind_tools(tools)


class State(TypedDict):
    message: Annotated[list, add_messages]


llm_graph = StateGraph(State)
