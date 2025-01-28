from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from src.session import session
from src.schemas import statement_schema
from src.services import statement_service
from src.repositories import statement_repository
from src.models import statement_model


router = APIRouter(prefix='/api/v1')

@router.post('/statement_add')
async def statement_add(statement_data: statement_schema.StatementSchemaAdd = Body(), session: AsyncSession = Depends(session.get_db_session))-> statement_schema.StatementSchemaAdd:
    service = statement_service.StatementService(session=session, repository=statement_repository.StatementRepository, model=statement_model.StatementModel)

    statement_new = await service.create(statement_data)

    return statement_new