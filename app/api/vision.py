from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.callmissed_client import CallMissedClient

router = APIRouter(
    prefix="/vision",
    tags=["Vision"]
)

client = CallMissedClient()


@router.post("")
async def vision(
    image: UploadFile = File(...),
    question: str = Form(...)
):

    ALLOWED_TYPES = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ]

    if image.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG and WEBP images are allowed."
        )

    image_bytes = await image.read()

    if len(image_bytes) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="Image size must be less than 5 MB."
        )

    if not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    answer = await client.vision(
        image_bytes=image_bytes,
        question=question
    )

    return {
        "answer": answer
    }
    
