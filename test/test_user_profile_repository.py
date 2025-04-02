import unittest
import pytest
from unittest import TestCase

from app.data.models.gender import Gender
from app.data.models.users.user_profile import User_Profile
from app.data.repository.user_profile_repository import UserRepository
from app.data.models.users.user import User

@pytest.mark.mongodb
class TestUserRepository(unittest.TestCase):

    UserRepository = UserRepository

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_user(self):
        user = User()
        user.email = "abojeedwin@gmail.com"
        user.pass_word = "password"
        user.user_name = "choko"
        user.user_profile = User_Profile()
        user.user_profile.gender = Gender.MALE
        user.user_profile.first_name = "Aboje"
        user.user_profile.last_name = "Edwin"
        user.user_profile.address = "Lagos"
        user.user_profile.age = "39"
        user.user_profile.phone_number = "+555555555"
        result = UserRepository.save(user)
        assert result.id is not None
