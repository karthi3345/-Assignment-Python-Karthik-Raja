import base64
import httpx

from app.core.config import settings
from app.core.config import settings
from app.exceptions.callmissed import CallMissedAPIException


class CallMissedClient:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.CALLMISSED_API_KEY

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    # ------------------------
    # Chat
    # ------------------------
    async def chat(self, history, message):

        messages = history + [
            {
                "role": "user",
                "content": message
            }
        ]

        payload = {
            "model": settings.CHAT_MODEL,
            "messages": messages
        }

        async with httpx.AsyncClient(timeout=60) as client:

            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload
            )

            print("CHAT:", response.status_code)
            print(response.text)

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

    # ------------------------
    # Image Generation
    # ------------------------
    async def generate_image(self, prompt: str):

        payload = {
            "model": settings.IMAGE_MODEL,
            "prompt": prompt,
            "n": 1
        }

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                f"{self.base_url}/images/generations",
                headers=self.headers,
                json=payload
            )

            print("IMAGE:", response.status_code)
            print(response.text)

            response.raise_for_status()

            return response.json()

    # ------------------------
    # Vision
    # ------------------------
    async def vision(self, image_bytes: bytes, question: str):

        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        payload = {
            "model": settings.CHAT_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ]
        }

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload
            )

            print("VISION:", response.status_code)
            print(response.text)

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]
        
def handle_response(self, response):

    if response.status_code == 402:
        raise CallMissedAPIException(
            402,
            "Payment Required"
        )

    if response.status_code == 403:
        raise CallMissedAPIException(
            403,
            "Invalid API Key"
        )

    if response.status_code == 429:
        raise CallMissedAPIException(
            429,
            "Too Many Requests"
        )

    if response.status_code >= 400:
        raise CallMissedAPIException(
            response.status_code,
            "CallMissed API Error"
        )