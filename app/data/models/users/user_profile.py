from dataclasses import dataclass
from app.data.models.gender import Gender


@dataclass
class User_Profile:
    id: str = None
    first_name: str = None
    last_name: str = None
    age: str = None
    gender: Gender = None
    phone_number: str = None
    address: str = None
