import unittest
import pytest

from app.data.models.gender import Gender
from app.data.models.users.user_profile import User_Profile
from app.data.repository.user_profile_repository import UserRepository
from app.data.models.users.user import User
from migrations.user_database import db

@pytest.mark.mongodb
class TestUserRepository(unittest.TestCase):

    UserRepository = UserRepository

    def setUp(self):
        db.users.delete_many({})

    def tearDown(self):
        db.users.delete_many({})

    def test_create_user(self):
        user = User()
        user.email = "abojeedwin@gmail.com"
        user.pass_word = "password"
        user.user_name = "choko"
        user.user_profile = User_Profile()
        user.user_profile.gender = Gender.MALE
        user.user_profile.first_name = "Aboje"
        user.user_profile.last_name = "Edwin"
        user.user_profile.address = "Ibadan"
        user.user_profile.age = "39"
        user.user_profile.phone_number = "+555555555"
        result = UserRepository.save(user)
        assert result.id is not None

    def test_delete_user(self):
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
        UserRepository.delete(user)
        assert UserRepository.count_documents() == 0

    def test_user_exists_by_email(self):
        assert UserRepository.count_documents() == 0
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
        self.assertFalse(UserRepository.exist_by_email("abojeedwi@gmail.com"))
        assert result.id is not None

    def test_user_exists_by_username(self):
        assert UserRepository.count_documents() == 0
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
        UserRepository.find_by_username("choko")
        assert result.id is not None

    def test_user_exists_by_user_name(self):
        assert UserRepository.count_documents() == 0
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
        UserRepository.exists_by_username("choko")
        assert result.id is not None

    def test_counts_of_users(self):
        assert UserRepository.count_documents() == 0
        user = User()
        user.email = "abojeedwin@gmail.com"
        user.pass_word = "password"
        user.user_name = "choko"
        user.user_profile = User_Profile()
        user.user_profile.gender = Gender.MALE
        user.user_profile.first_name = "Aboje"
        user.user_profile.last_name = "Edwin"
        UserRepository.save(user)

        user1 = User()
        user1.email = "jagz@gmail.com"
        user1.pass_word = "password"
        user1.user_name = "salamanda"
        user1.user_profile = User_Profile()
        user1.user_profile.gender = Gender.FEMALE
        user1.user_profile.first_name = "Abraham"
        user1.user_profile.last_name = "Sarah"
        UserRepository.save(user1)

        assert UserRepository.count_documents() == 2



    def test_find_user_by_id(self):
        assert UserRepository.count_documents() == 0
        user = User()
        user.email = "abojeedwin@gmail.com"
        user.pass_word = "password"
        user.user_name = "choko"
        user.user_profile = User_Profile()
        user.user_profile.gender = Gender.MALE
        user.user_profile.first_name = "Aboje"
        user.user_profile.last_name = "Edwin"
        UserRepository.save(user)
        self.assertTrue(UserRepository.exists_by_id(user.id))


    def test_delete_user_by_id(self):
        assert UserRepository.count_documents() == 0
        user = User()
        user.email = "abojeedwin@gmail.com"
        user.pass_word = "password"
        user.user_name = "choko"
        user.user_profile = User_Profile()
        user.user_profile.gender = Gender.MALE
        user.user_profile.first_name = "Aboje"
        user.user_profile.last_name = "Edwin"
        saved_user = UserRepository.save(user)
        UserRepository.delete_by_id(saved_user.id)
        assert UserRepository.count_documents() == 0

    def test_delete_users_by_id(self):
        users_ids = []
        assert UserRepository.count_documents() == 0
        user = User()
        user.email = "abojeedwin@gmail.com"
        user.pass_word = "password"
        user.user_name = "choko"
        user.user_profile = User_Profile()
        user.user_profile.gender = Gender.MALE
        user.user_profile.first_name = "Aboje"
        user.user_profile.last_name = "Edwin"
        UserRepository.save(user)

        user1 = User()
        user1.email = "jagz@gmail.com"
        user1.pass_word = "password"
        user1.user_name = "salamanda"
        user1.user_profile = User_Profile()
        user1.user_profile.gender = Gender.FEMALE
        user1.user_profile.first_name = "Abraham"
        user1.user_profile.last_name = "Sarah"
        UserRepository.save(user1)
        users_ids.append(user.id)
        users_ids.append(user1.id)

        assert UserRepository.count_documents() == 2
        UserRepository.delete_users_by_id(users_ids)
        assert UserRepository.count_documents() == 0

    def test_update_user_by_id(self):
        assert UserRepository.count_documents() == 0
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
        UserRepository.save(user)
        self.assertFalse(UserRepository.exist_by_email("abojeedwi@gmail.com"))
        UserRepository.update(user, user.id)
        assert UserRepository.count_documents() == 1

