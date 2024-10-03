from pydantic import BaseModel


class PresentationCreate(BaseModel):
    url: str
    description: str
    specs: str
    category: str
