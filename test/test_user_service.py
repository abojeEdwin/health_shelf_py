import unittest
from datetime import datetime

import pytest
from app.data.models.gender import Gender
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.data.repository.appointment_repository import AppointmentRepository
from app.services.Dto.appointment_request import User_Appointment_Request
from app.services.Dto.user_login_request import User_Login_Request
from app.services.Dto.user_registration_request import User_Registration_Request
from app.services.user_service import UserService
from app.exceptions.duplicate_email_exception import Duplicate_Email_Exception
from app.exceptions.duplicate_username_exception import Duplicate_Username_Exception
from app.exceptions.invalid_password_exception import Invalid_Password_Exception
from migrations.appointment_database import db


@pytest.mark.mongodb
class TestUserService(unittest.TestCase):

    request = User_Registration_Request()
    UserService = UserService
    AppointmentRepository = AppointmentRepository


    def setUp(self):
        UserService.delete_all()
        db.appointments.delete_many({})


    def tearDown(self):
        UserService.delete_all()
        db.appointments.delete_many({})


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

    def test_user_cannot_register_twice(self):
        request = User_Registration_Request()
        request.user = User()
        request.user.user_name = "mad mike007"
        request.user.pass_word = "password"
        request.user.email = "email@gmail.com"
        request.user.user_profile = User_Profile()
        request.user.user_profile.first_name = "micheal"
        request.user.user_profile.last_name = "sam"
        request.user.user_profile.gender = Gender.MALE
        request.user.user_profile.address = "123 Main St"
        request.user.user_profile.age = "30"
        request.user.user_profile.phone_number = "+1234567890"
        UserService.register(request)

        second_request = User_Registration_Request()
        request = User_Registration_Request()
        second_request.user = User()
        second_request.user.user_name = "mad mike"
        second_request.user.pass_word = "password"
        second_request.user.email = "email@gmail.com"
        second_request.user.user_profile = User_Profile()
        second_request.user.user_profile.first_name = "micheal"
        second_request.user.user_profile.last_name = "sam"
        second_request.user.user_profile.gender = Gender.MALE
        second_request.user.user_profile.address = "123 Main St"
        second_request.user.user_profile.age = "30"
        second_request.user.user_profile.phone_number = "+1234567890"
        self.assertRaises(Duplicate_Email_Exception,UserService.register,second_request)

    def test_user_cannot_register_with_same_user_name_twice(self):
        request = User_Registration_Request()
        request.user = User()
        request.user.user_name = "mad mike"
        request.user.pass_word = "password"
        request.user.email = "uniqueemail200@gmail.com"
        request.user.user_profile = User_Profile()
        request.user.user_profile.first_name = "micheal"
        request.user.user_profile.last_name = "sam"
        request.user.user_profile.gender = Gender.MALE
        request.user.user_profile.address = "123 Main St"
        request.user.user_profile.age = "30"
        request.user.user_profile.phone_number = "+1234567890"
        UserService.register(request)

        second_request = User_Registration_Request()
        second_request.user = User()
        second_request.user.user_name = "mad mike"
        second_request.user.pass_word = "password"
        second_request.user.email = "uniqueemail@gmail.com"
        second_request.user.user_profile = User_Profile()
        second_request.user.user_profile.first_name = "micheal"
        second_request.user.user_profile.last_name = "sam"
        second_request.user.user_profile.gender = Gender.MALE
        second_request.user.user_profile.address = "123 Main St"
        second_request.user.user_profile.age = "30"
        second_request.user.user_profile.phone_number = "+1234567890"
        self.assertRaises(Duplicate_Username_Exception,UserService.register,second_request)


    def test_user_login(self):
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
        login_request = User_Login_Request()
        login_request.email = "email@gmail.com"
        login_request.password = "password"
        result2 = UserService.login(login_request)
        assert result2["email"] == "email@gmail.com"


    def test_user_login_with_valid_password(self):
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
        login_request = User_Login_Request()
        login_request.email = "email@gmail.com"
        login_request.password = "passwor"
        self.assertRaises(Invalid_Password_Exception,UserService.login,login_request)


    def test_find_user_by_id(self):
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
        result_id = result.id
        assert result.id is not None
        login_request = User_Login_Request()
        login_request.email = "email@gmail.com"
        login_request.password = "password"
        user_login = UserService.login(login_request)
        assert user_login["_id"] == result_id
        self.assertTrue(UserService.find_by_id(result_id))

    def test_find_all_users(self):
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
        result_id = result.id
        assert result.id is not None
        assert UserService.find_all() == 1


    def test_delete_account_by_id(self):
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
        result_id = result.id
        assert result.id is not None
        UserService.delete_by_id(result_id)
        assert UserService.count() == 0


    def test_user_create_appointment(self):
        request = User_Appointment_Request()
        request.appointment.patient = User()
        request.appointment.patient.first_name = "dele"
        request.appointment.patient.last_name = "kasongo"
        request.appointment.patient.pass_word = "password"
        request.appointment.patient.email = "trojan@gmail.com"
        request.appointment.patient.user_profile = User_Profile()
        request.appointment.patient.user_profile.first_name = "dele"
        request.appointment.patient.user_profile.gender = Gender.FEMALE
        request.appointment.patient.user_profile.address = "London, UK"
        request.appointment.doctor = Doctor()
        request.appointment.doctor.first_name = "doctor injection"
        request.appointment.doctor.last_name = "you no go cry ke?"
        request.appointment.doctor.user_name = "masha"
        request.appointment.doctor.password = "password"
        request.appointment.doctor.email = "jagaga@gmail.com"
        request.appointment.doctor.doctor_profile = Doctor_Profile()
        request.appointment.doctor.doctor_profile.age = "200"
        request.appointment.doctor.doctor_profile.specialty = "Agbo doctor"
        request.appointment.doctor.doctor_profile.phone_number = "+2348899023"
        request.appointment.doctor.doctor_profile.address = "Abuja"
        request.appointment.doctor.doctor_profile.gender = Gender.MALE
        request.appointment.appointment_details = " You have Corona Virus"
        request.appointment.local_time = datetime.now()
        result = UserService.create_appointment(request)
        assert result.id is not None

    def test_find_all_appointments(self):
        request = User_Appointment_Request()
        request.appointment.patient = User()
        request.appointment.patient.first_name = "dele"
        request.appointment.patient.last_name = "kasongo"
        request.appointment.patient.pass_word = "password"
        request.appointment.patient.email = "trojan@gmail.com"
        request.appointment.patient.user_profile = User_Profile()
        request.appointment.patient.user_profile.first_name = "dele"
        request.appointment.patient.user_profile.gender = Gender.FEMALE
        request.appointment.patient.user_profile.address = "London, UK"
        request.appointment.doctor = Doctor()
        request.appointment.doctor.first_name = "doctor injection"
        request.appointment.doctor.last_name = "you no go cry ke?"
        request.appointment.doctor.user_name = "masha"
        request.appointment.doctor.password = "password"
        request.appointment.doctor.email = "jagaga@gmail.com"
        request.appointment.doctor.doctor_profile = Doctor_Profile()
        request.appointment.doctor.doctor_profile.age = "200"
        request.appointment.doctor.doctor_profile.specialty = "Agbo doctor"
        request.appointment.doctor.doctor_profile.phone_number = "+2348899023"
        request.appointment.doctor.doctor_profile.address = "Abuja"
        request.appointment.doctor.doctor_profile.gender = Gender.MALE
        request.appointment.appointment_details = " You have Corona Virus"
        request.appointment.local_time = datetime.now()
        result = UserService.create_appointment(request)
        assert result.id is not None
        assert UserService.find_all_appointments()

    def test_get_all_appointments(self):
        request = User_Appointment_Request()
        request.appointment.patient = User()
        request.appointment.patient.first_name = "dele"
        request.appointment.patient.last_name = "kasongo"
        request.appointment.patient.pass_word = "password"
        request.appointment.patient.email = "trojan@gmail.com"
        request.appointment.patient.user_profile = User_Profile()
        request.appointment.patient.user_profile.first_name = "dele"
        request.appointment.patient.user_profile.gender = Gender.FEMALE
        request.appointment.patient.user_profile.address = "London, UK"
        request.appointment.doctor = Doctor()
        request.appointment.doctor.first_name = "doctor injection"
        request.appointment.doctor.last_name = "you no go cry ke?"
        request.appointment.doctor.user_name = "masha"
        request.appointment.doctor.password = "password"
        request.appointment.doctor.email = "jagaga@gmail.com"
        request.appointment.doctor.doctor_profile = Doctor_Profile()
        request.appointment.doctor.doctor_profile.age = "200"
        request.appointment.doctor.doctor_profile.specialty = "Agbo doctor"
        request.appointment.doctor.doctor_profile.phone_number = "+2348899023"
        request.appointment.doctor.doctor_profile.address = "Abuja"
        request.appointment.doctor.doctor_profile.gender = Gender.MALE
        request.appointment.appointment_details = " You have Corona Virus"
        request.appointment.local_time = datetime.now()
        result = UserService.create_appointment(request)
        assert result.id is not None
        appointment = UserService.get_appointment(result.id)
        assert appointment is not None

    def test_find_all_doctors(self):
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
        login_request = User_Login_Request()
        login_request.email = "email@gmail.com"
        login_request.password = "password"
        result2 = UserService.login(login_request)
        assert result2["email"] == "email@gmail.com"






