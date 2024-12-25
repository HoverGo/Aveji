from src.services.base_service import BaseService


class StatementService(BaseService):
    async def create(self, statement_data):
        statement_new = await super().create(statement_data)
        return statement_new