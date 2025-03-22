from src.database import ParkingSpaceLog


class Repository:
    @staticmethod
    async def get_count_of_occupied_spaces() -> int:
        return await ParkingSpaceLog.find({"is_active": True}).count()

    @staticmethod
    async def get_occupied_spaces() -> list[ParkingSpaceLog]:
        return await ParkingSpaceLog.find({"is_active": True}).to_list()
    
    @staticmethod
    async def get_parking_space_log_by_place_number(place_number: int) -> ParkingSpaceLog | None:
        return await ParkingSpaceLog.find_one({"place_number": place_number, "is_active": True})

    @staticmethod
    async def add_parking_space_log(
        parking_space_log: ParkingSpaceLog,
    ) -> ParkingSpaceLog:
        return await parking_space_log.insert()

    @staticmethod
    async def get_parking_space_logs_by_first_name_and_last_name(
        first_name: str, last_name: str
    ) -> list[ParkingSpaceLog]:
        return await ParkingSpaceLog.find(
            {"first_name": first_name, "last_name": last_name, "is_active": True}
        ).to_list()
    
    @staticmethod
    async def update_parking_space_log(parking_space_log: ParkingSpaceLog) -> ParkingSpaceLog:
        return await parking_space_log.save()
