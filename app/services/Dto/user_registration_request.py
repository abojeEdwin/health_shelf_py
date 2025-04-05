from dataclasses import dataclass
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile

@dataclass
class User_Registration_Request:
    user : User = None
    user_profile : User_Profile = None
