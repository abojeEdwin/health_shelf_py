from dataclasses import dataclass
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
import bcrypt



@dataclass
class User_Login_Request:
    email : str = None
    password: str = None



