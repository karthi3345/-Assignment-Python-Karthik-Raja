from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.api.health import router as health_router
from app.api.chat import router as chat_router
from app.api.image import router as image_router
from app.api.vision import router as vision_router

from app.exceptions.callmissed import CallMissedAPIException
from app.exceptions.handlers import (
    callmissed_exception_handler,
    generic_exception_handler,
)

app = FastAPI(
    title="Backend Chatbot API",
    version="1.0.0",
    description="Python Backend Engineer Assignment"
)

# Templates
templates = Jinja2Templates(directory="templates")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(image_router)
app.include_router(vision_router)

# Home Page
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# Exception Handlers
app.add_exception_handler(
    CallMissedAPIException,
    callmissed_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)