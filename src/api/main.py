import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router
from src.database.db import initialize_database
from src.settings import settings

logging.basicConfig(
    format=settings.LOGGING_FORMAT,
    datefmt=settings.LOGGING_DATE_FORMAT,
    level=settings.LOGGING_LEVEL,
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await initialize_database()
    logger.info("Application startup")
    yield
    # after finishing
    logger.info("Application shutdown")


ROUTERS = [router]

app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_TITLE,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in ROUTERS:
    app.include_router(router)
