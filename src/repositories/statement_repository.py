from src.repositories.base_repository import BaseRepository
from src.schemas import statement_schema


class StatementRepository(BaseRepository):
    async def create(self, statement_data: statement_schema.StatementSchemaAdd) -> statement_schema.StatementSchemaAdd:
        statement_new = await super().create(statement_data)
        return statement_new