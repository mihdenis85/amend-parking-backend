from fastapi import APIRouter, Depends

from src.api.auth import APIKeyAuth
from src.api.schemas import AddParkingSpaceLogSchema
from src.api.service import Service
from src.database import ParkingSpaceLog
from src.settings import settings

router = APIRouter(
    tags=["Parking"],
    prefix="/parking",
    dependencies=[Depends(APIKeyAuth(settings.PARKING_SERVICE_API_KEY))],
)


@router.get("/free-spaces-count", response_model=int)
async def get_count_of_free_spaces():
    """Get the count of free spaces.

    Returns:
        The count of free spaces.
    """
    return await Service.get_count_of_free_spaces()


@router.get("/occupied-spaces-list", response_model=list[ParkingSpaceLog])
async def get_occupied_spaces():
    """Get the list of occupied spaces.

    Returns:
        The list of occupied spaces.
    """
    return await Service.get_occupied_spaces()


@router.post("/park-car", response_model=ParkingSpaceLog)
async def park_car(body: AddParkingSpaceLogSchema):
    """Park a car.

    Returns:
        The parking space log.

    Raises:
        HTTPException (400): If the parking space is already occupied.
    """
    return await Service.add_parking_space_log(
        place_number=body.place_number,
        first_name=body.first_name,
        last_name=body.last_name,
        car_make=body.car_make,
        license_plate=body.license_plate,
    )


@router.post("/free-up", response_model=ParkingSpaceLog)
async def free_up_parking_space(place_number: int):
    """Free up a parking space.

    Args:

    - **place_number**: The place number of the parking space.

    Returns:
        The parking space log.

    Raises:
        HTTPException (400): If the parking space is already free.
    """
    return await Service.free_up_parking_space(place_number)


@router.get("/parking-space-logs", response_model=list[ParkingSpaceLog])
async def get_parking_space_logs(first_name: str, last_name: str):
    """Get the parking space logs by first name and last name.

    Args:

    - **first_name**: The first name of the person.
    - **last_name**: The last name of the person.

    Returns:
        The list of parking space logs.
    """
    return await Service.get_parking_space_logs_by_first_name_and_last_name(
        first_name, last_name
    )
