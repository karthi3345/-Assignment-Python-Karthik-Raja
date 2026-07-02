from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.callmissed import CallMissedAPIException


async def callmissed_exception_handler(
    request: Request,
    exc: CallMissedAPIException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error"
        }
    )