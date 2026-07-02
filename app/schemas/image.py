from pydantic import BaseModel, Field


class ImageRequest(BaseModel):
    prompt: str = Field(..., min_length=1)


class ImageResponse(BaseModel):
    image: str
    
    
# validate 
prompt: str = Field(
    ...,
    min_length=3,
    max_length=1000
)