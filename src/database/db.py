import logging

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

from src.settings import settings
from src.database import MODELS

logger = logging.getLogger(__name__)

client = AsyncIOMotorClient(settings.MONGODB_URL)


async def initialize_database():
    try:
        await init_beanie(database=client.ParkingService, document_models=MODELS)
        logger.info("Database initialized successfully.")
    except ConnectionFailure as e:
        logger.error(f"Connection error during database initialization: {e}")
        raise e
