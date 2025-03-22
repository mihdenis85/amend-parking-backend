import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LOGGING_FORMAT: str = (
        "%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in function %(funcName)s] %(message)s"
    )
    LOGGING_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    LOGGING_LEVEL: int = logging.INFO

    MONGODB_URL: str = "mongodb://mongodb:27017"
    APP_TITLE: str = "Parking Service"
    DB_NAME: str = "ParkingService"

    PARKING_SERVICE_API_KEY: str = Field(...)

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
