from src.models.base_model import BaseModel
from src.schemas.base_schema import BaseSchema


class BaseRepository():
    
    def __init__(self, session, model: BaseModel) -> None:
        self.session = session
        self.model = model

    async def create(self, instance_data: BaseSchema) -> BaseSchema:
        data = instance_data.model_dump()
        instance_new = self.model(**data)
        self.session.add(instance_new)
        await self.session.flush()
        await self.session.commit()
        return instance_new
