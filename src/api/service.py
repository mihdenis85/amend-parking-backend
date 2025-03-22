import uuid
from datetime import datetime, timezone

from fastapi import HTTPException, status

from src.api.repository import Repository
from src.database import ParkingSpaceLog
from src.settings import settings


class Service:
    @staticmethod
    async def get_count_of_free_spaces() -> int:
        return (
            settings.PARKING_SLOTS_COUNT
            - await Repository.get_count_of_occupied_spaces()
        )

    @staticmethod
    async def get_occupied_spaces() -> list[ParkingSpaceLog]:
        return await Repository.get_occupied_spaces()

    @staticmethod
    async def add_parking_space_log(
        place_number: int,
        first_name: str,
        last_name: str,
        car_make: str,
        license_plate: str,
    ) -> ParkingSpaceLog:
        if await Repository.get_parking_space_log_by_place_number(place_number) is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parking space is already occupied",
            )

        parking_space_log = ParkingSpaceLog(
            log_id=uuid.uuid4(),
            place_number=place_number,
            first_name=first_name,
            last_name=last_name,
            car_make=car_make,
            license_plate=license_plate,
            created_at=datetime.now(timezone.utc),
            is_active=True,
        )
        return await Repository.add_parking_space_log(parking_space_log)

    @staticmethod
    async def free_up_parking_space(place_number: int) -> ParkingSpaceLog:
        parking_space_log = await Repository.get_parking_space_log_by_place_number(
            place_number
        )

        if parking_space_log is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parking space is already free",
            )

        parking_space_log.is_active = False
        parking_space_log.free_up_time = datetime.now(timezone.utc)
        return await Repository.update_parking_space_log(parking_space_log)

    @staticmethod
    async def get_parking_space_logs_by_first_name_and_last_name(
        first_name: str, last_name: str
    ) -> list[ParkingSpaceLog]:
        return await Repository.get_parking_space_logs_by_first_name_and_last_name(
            first_name, last_name
        )
