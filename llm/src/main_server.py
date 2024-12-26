from typing import Annotated, Literal, TypedDict

from fastapi import FastAPI
# from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
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
