from dataclasses import dataclass
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile



@dataclass
class User_Registration_Request:
    user : User = None
    user_profile : User_Profile = None
    # def __init__(self, user_name: str, password: str, email: str, user_profile: User_Profile):
    #     self.user_name = user_name
    #     self.password = password
    #     self.email = email
    #     self.user_profile = user_profile