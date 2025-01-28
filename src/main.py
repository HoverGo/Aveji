from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router
from contextlib import asynccontextmanager
from src.session import session


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный контекстный менеджер, обрабатывающий вход и выход из приложения"""
    print('App is open')
    await session.init_models()
    yield
    print('App is closed')


app = FastAPI(lifespan=lifespan)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы со всех источников (или укажите конкретные домены)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, OPTIONS и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)