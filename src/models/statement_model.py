from src.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

class StatementModel(BaseModel):
    __tablename__ = 'statements'

    name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]