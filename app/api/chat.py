from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.callmissed_client import CallMissedClient

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

client = CallMissedClient()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:

        history = [msg.model_dump() for msg in request.history]

        reply = await client.chat(
            history,
            request.message
        )

        return ChatResponse(reply=reply)

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to process your request."
        )