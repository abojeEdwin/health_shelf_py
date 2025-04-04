import unittest
import pytest

from app.data.models.gender import Gender
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.data.repository.user_profile_repository import UserRepository
from app.services.Dto.user_registration_request import User_Registration_Request
from app.services.user_service import UserService
from migrations.user_profile_database import db

@pytest.mark.mongodb
class TestUserService(unittest.TestCase):

    request = User_Registration_Request()
    UserService = UserService

    def setUp(self):
        UserService.delete_all()

    def tearDown(self):
        UserService.delete_all()


    def test_user_can_register(self):
        request = User_Registration_Request()
        request.user = User()
        request.user.user_name = "mad mike"
        request.user.pass_word = "password"
        request.user.email = "email@gmail.com"
        request.user.user_profile = User_Profile()
        request.user.user_profile.first_name = "micheal"
        request.user.user_profile.last_name = "sam"
        request.user.user_profile.gender = Gender.MALE
        request.user.user_profile.address = "123 Main St"
        request.user.user_profile.age = "30"
        request.user.user_profile.phone_number = "+1234567890"
        result = UserService.register(request)
        assert result.id is not None
        assert result.user_name == "mad mike"
        assert UserService.count() == 1

