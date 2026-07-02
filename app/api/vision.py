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

    try:

        image_bytes = await image.read()

        answer = await client.vision(
            image_bytes,
            question
        )

        return {
            "answer": answer
        }

    except Exception as e:
        import traceback
        traceback.print_exc()

    raise HTTPException(
        status_code=500,
        detail=str(e)
    )