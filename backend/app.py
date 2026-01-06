from fastapi import FastAPI
from pydantic import BaseModel
from backend.chatbot import get_chat_response

app = FastAPI(title="LLM Chatbot API")


class ChatRequest(BaseModel):
    message: str
    history: list = []


@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_chat_response(
        user_message=request.message,
        chat_history=request.history
    )
    return {"response": reply}
