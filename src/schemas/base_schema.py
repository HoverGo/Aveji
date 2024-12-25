from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True # Позволяет работать не только с dict при получении данных, а так же с полями объектов моделей через '.'