from datetime import datetime
from uuid import UUID

from beanie import Document


class ParkingSpaceLog(Document):
    log_id: UUID

    place_number: int
    first_name: str
    last_name: str
    car_make: str
    license_plate: str
    created_at: datetime

    is_active: bool = True
    free_up_time: datetime | None = None

    class Settings:
        name = "parking_space_logs"
