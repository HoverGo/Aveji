from fastapi import FastAPI
from src.routes import router
from contextlib import asynccontextmanager
from src.session import session


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный контекстный менеджер, обрабатывающий вход и выход из приложения"""
    print('App is open')
    session.init_models()
    yield
    print('App is closed')


app = FastAPI(lifespan=lifespan)
app.include_router(router)