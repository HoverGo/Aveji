from src.schemas.base_schema import BaseSchema
from pydantic import EmailStr, field_validator
import re


class StatementSchemaAdd(BaseSchema):
    name: int
    email: EmailStr
    phone: str

    @field_validator('phone')
    def phone_validator(cls, v):
        phone_pattern = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"

        if not re.match(phone_pattern, v):
            raise ValueError('Phone do not match')
        
        return v