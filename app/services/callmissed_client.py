import httpx

from app.core.config import settings


class CallMissedClient:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.CALLMISSED_API_KEY

    async def chat(self, history, message):

        messages = history + [
            {
                "role": "user",
                "content": message
            }
        ]

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": settings.CHAT_MODEL,
            "messages": messages
        }

        async with httpx.AsyncClient(timeout=60) as client:

            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]