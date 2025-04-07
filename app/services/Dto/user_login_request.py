from dataclasses import dataclass

@dataclass
class User_Login_Request:
    email : str = None
    password: str = None



