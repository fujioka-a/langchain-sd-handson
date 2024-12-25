from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0"
)

add_routes(
    app,
    ChatOpenAI(model="gpt-3.5-turbo"),
    path='./openai'
)
