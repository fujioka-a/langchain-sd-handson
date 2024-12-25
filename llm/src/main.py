from typing import Annotated, Literal, TypedDict

from fastapi import FastAPI
# from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langserve import add_routes

# 基本設定 =================
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

# modelへのツール登録 =====


@tool
def weather(query: str):
    """"今日の天気を返す"""
    # return f"Today's weather is sunny in {query}."
    return "晴れのち雨です"


tools = [weather]
llm_model = llm_model.bind_tools(tools)


# グラフ定義 ==============
class State(TypedDict):
    message: Annotated[list, add_messages]


llm_graph = StateGraph(State)


# ノードとエッジの定義 ==============
def call_model(state: State, config: RunnableConfig):
    message = state['messages']
    response = llm_model(message)
    return {'message': response}


tool_node = ToolNode(tools)


def should_continue(state: State) -> Literal['__end__', 'tools']:
    messages = state['messages']
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return 'tools'


llm_graph.add_node('agent', call_model)
llm_graph.add_node('tools', tool_node)

llm_graph.add_edge(START, 'agent')
llm_graph.add_conditional_edges('agent', should_continue)
llm_graph.add_edge('tools', 'agent')

compiled = llm_graph.compile()
