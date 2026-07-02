from fastapi import APIRouter, HTTPException

from app.schemas.image import ImageRequest
from app.services.callmissed_client import CallMissedClient

router = APIRouter(
    prefix="/image",
    tags=["Image"]
)

client = CallMissedClient()


@router.post("")
async def generate_image(request: ImageRequest):

    try:
        return await client.generate_image(request.prompt)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Image generation failed."
        )