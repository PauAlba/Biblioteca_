from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None #indicamos que es opcional
    title: str = Field(min_length=5, max_length = 50)
    autor: str = Field(min_length=5, max_length = 50)
    year: int = Field(default=2000, le = 2025)
    category: str
    pages: int = Field(default=200, le = 5000)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi libro",
                "autor": "Nombre del autor",
                "year": 2025,
                "category": "Accion",
                "pages": 200
            }
        }