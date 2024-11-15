import uvicorn
from fastapi import FastAPI
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langserve import add_routes

DEFAULT_MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"

app = FastAPI()

chat = ChatBedrock(model_id=DEFAULT_MODEL_ID)

prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | chat

add_routes(app, chain, playground_type="chat")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
