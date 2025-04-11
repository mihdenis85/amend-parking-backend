from pydantic import BaseModel, ConfigDict


class AddParkingSpaceLogSchema(BaseModel):
    """
    Schema for adding a parking space log.
    """

    model_config = ConfigDict(use_attribute_docstrings=True)

    first_name: str
    """
    The first name of the person.
    """

    last_name: str
    """
    The last name of the person.
    """

    car_make: str
    """
    The car make of the person.
    """

    license_plate: str
    """
    The license plate of the car.
    """
