from dataclasses import dataclass
from app.data.models.users.user_profile import User_Profile


@dataclass
class User:
    id : str = None
    user_name : str = None
    email : str =  None
    pass_word : str = None
    user_profile : User_Profile = None
