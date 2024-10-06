from typing import Optional

from pydantic import BaseModel


class PresentationCreate(BaseModel):
    url: Optional[str]
    description: Optional[str]
    specs: Optional[str]
    category: Optional[str]
