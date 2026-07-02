from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CALLMISSED_API_KEY: str
    BASE_URL: str

    CHAT_MODEL: str
    IMAGE_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()