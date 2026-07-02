from pydantic import BaseModel, Field
from typing import List, Literal


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: List[Message] = []


class ChatResponse(BaseModel):
    reply: str