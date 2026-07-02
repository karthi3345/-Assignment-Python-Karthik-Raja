from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.chat import router as chat_router
from app.api.image import router as image_router
from app.api.vision import router as vision_router

app = FastAPI(
    title="Backend Chatbot API",
    version="1.0.0",
    description="Python Backend Engineer Assignment"
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(image_router)
app.include_router(vision_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Backend Chatbot API"
    }