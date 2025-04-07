import unittest
from datetime import datetime
from unittest.mock import patch

import pytest

from app.data.models.gender import Gender
from app.data.models.medical_history import Medical_History
from app.data.models.speciality import Speciality
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.exceptions.duplicate_email_exception import Duplicate_Email_Exception
from app.exceptions.duplicate_username_exception import Duplicate_Username_Exception
from app.exceptions.invalid_password_exception import Invalid_Password_Exception
from app.exceptions.user_not_found_exception import User_Not_Found_Exception
from app.services.Dto.appointment_request import User_Appointment_Request
from app.services.Dto.doctor_registration_request import Doctor_Registration_Request
from app.services.Dto.medical_history_request import Medical_History_Request
from app.services.Dto.user_login_request import User_Login_Request
from app.services.doctor_service import DoctorService
from app.data.repository.appointment_repository import AppointmentRepository

@pytest.mark.mongodb
class TestDoctorService(unittest.TestCase):

    request = Doctor_Registration_Request
    DoctorService = DoctorService
    AppointmentRepository = AppointmentRepository

    def setUp(self):
        DoctorService.delete_all()

    def tearDown(self):
        DoctorService.delete_all()

    def test_doctor_register(self):
        request =  Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None
        assert DoctorService.count_documents() == 1

    def test_doctor_register_twice_(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None

        request1 = Doctor_Registration_Request()
        request1.user = User()
        request1.user.user_name = "mad mike"
        request1.user.pass_word = "password"
        request1.user.email = "email@gmail.com"
        request1.user.user_profile = User_Profile()
        request1.user.user_profile.first_name = "micheal"
        request1.user.user_profile.last_name = "sam"
        request1.user.user_profile.gender = Gender.MALE
        request1.user.user_profile.address = "123 Main St"
        request1.user.user_profile.age = "30"
        request1.user.user_profile.phone_number = "+1234567890"
        request1.doctor = Doctor()
        request1.doctor.first_name = "doctor injection"
        request1.doctor.last_name = "you no go cry ke?"
        request1.doctor.user_name = "masha"
        request1.doctor.password = "password"
        request1.doctor.email = "jagaga@gmail.com"
        request1.doctor.doctor_profile = Doctor_Profile()
        request1.doctor.doctor_profile.age = "200"
        request1.doctor.doctor_profile.specialty = "Agbo doctor"
        request1.doctor.doctor_profile.phone_number = "+2348899023"
        request1.doctor.doctor_profile.address = "Abuja"
        request1.doctor.doctor_profile.gender = Gender.MALE
        request1.doctor_profile.specialty = Speciality()
        request1.doctor_profile.specialty.specialty = "Agbo Doctor"
        request1.local_time = datetime.now()
        self.assertRaises(Duplicate_Email_Exception,DoctorService.register,request1)
        assert result.id is not None

    def test_user_cannot_register_with_same_username(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None

        request1 = Doctor_Registration_Request()
        request1.user = User()
        request1.user.user_name = "mad mike"
        request1.user.pass_word = "password"
        request1.user.email = "email@gmail.com"
        request1.user.user_profile = User_Profile()
        request1.user.user_profile.first_name = "micheal"
        request1.user.user_profile.last_name = "sam"
        request1.user.user_profile.gender = Gender.MALE
        request1.user.user_profile.address = "123 Main St"
        request1.user.user_profile.age = "30"
        request1.user.user_profile.phone_number = "+1234567890"
        request1.doctor = Doctor()
        request1.doctor.first_name = "doctor injection"
        request1.doctor.last_name = "you no go cry ke?"
        request1.doctor.user_name = "masha"
        request1.doctor.password = "password"
        request1.doctor.email = "jaga@gmail.com"
        request1.doctor.doctor_profile = Doctor_Profile()
        request1.doctor.doctor_profile.age = "200"
        request1.doctor.doctor_profile.specialty = "Agbo doctor"
        request1.doctor.doctor_profile.phone_number = "+2348899023"
        request1.doctor.doctor_profile.address = "Abuja"
        request1.doctor.doctor_profile.gender = Gender.MALE
        request1.doctor_profile.specialty = Speciality()
        request1.doctor_profile.specialty.specialty = "Agbo Doctor"
        request1.local_time = datetime.now()
        self.assertRaises(Duplicate_Username_Exception, DoctorService.register, request1)
        assert result.id is not None

    def test_doctor_login(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None
        doctor_login_request = User_Login_Request()
        doctor_login_request.password = "password"
        doctor_login_request.email = "jagaga@gmail.com"
        result = DoctorService.login(doctor_login_request)
        assert result["email"] == "jagaga@gmail.com"

    def test_doctor_login_with_invalid_password(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None
        doctor_login_request = User_Login_Request()
        doctor_login_request.password = "word"
        doctor_login_request.email = "jagaga@gmail.com"
        self.assertRaises(Invalid_Password_Exception,DoctorService.login,doctor_login_request)


    def test_doctor_not_found_raise_exception(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None
        doctor_login_request = User_Login_Request()
        doctor_login_request.password = "word"
        doctor_login_request.email = "jag@gmail.com"
        self.assertRaises(User_Not_Found_Exception,DoctorService.login,doctor_login_request)

    def test_create_appointment(self):
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
        result = DoctorService.create_appointment(request)
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
        result = DoctorService.create_appointment(request)
        assert result.id is not None
        assert DoctorService.find_all_appointments()

    def test_find_all_doctors(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        assert result.id is not None
        doctor_login_request = User_Login_Request()
        doctor_login_request.password = "password"
        doctor_login_request.email = "jagaga@gmail.com"
        result = DoctorService.login(doctor_login_request)
        assert result["email"] == "jagaga@gmail.com"
        doctor_list = DoctorService.find_all()
        assert doctor_list == 1

    def test_delete_account_by_id(self):
        request = Doctor_Registration_Request()
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
        request.doctor = Doctor()
        request.doctor.first_name = "doctor injection"
        request.doctor.last_name = "you no go cry ke?"
        request.doctor.user_name = "masha"
        request.doctor.password = "password"
        request.doctor.email = "jagaga@gmail.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.age = "200"
        request.doctor.doctor_profile.specialty = "Agbo doctor"
        request.doctor.doctor_profile.phone_number = "+2348899023"
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor_profile.specialty = Speciality()
        request.doctor_profile.specialty.specialty = "Agbo Doctor"
        request.local_time = datetime.now()
        result = DoctorService.register(request)
        doctor_id = result.id
        assert doctor_id is not None
        doctor_login_request = User_Login_Request()
        doctor_login_request.password = "password"
        doctor_login_request.email = "jagaga@gmail.com"
        result = DoctorService.login(doctor_login_request)
        assert result["email"] == "jagaga@gmail.com"
        DoctorService.delete_by_id(doctor_id)
        assert DoctorService.count_documents() == 0

    def test_doctor_create_medical_history(self):
        request = Medical_History_Request()
        request.medical_history_details = "Your medical history details"
        request.patient = User()
        request.patient.user_name = "user_name"
        request.patient.pass_word = "pass_word"
        request.patient.email = "email@example.com"
        request.patient.user_profile = User_Profile()
        request.patient.user_profile.first_name = "first_name"
        request.patient.user_profile.last_name = "last_name"
        request.patient.user_profile.gender = Gender.MALE
        request.patient.user_profile.address = "Abuja"
        request.patient.user_profile.age = "79"
        request.patient.user_profile.phone_number = "+23477665532"
        request.doctor = Doctor()
        request.doctor.user_name = "doc kiriku"
        request.doctor.password = "password"
        request.doctor.email = "doc@example.com"
        request.doctor.doctor_profile = Doctor_Profile()
        request.doctor.doctor_profile.phone_number = "+23477665532"
        request.doctor.doctor_profile.gender = Gender.MALE
        request.doctor.doctor_profile.address = "Abuja"
        request.doctor.doctor_profile.age = "60"
        request.doctor.doctor_profile.first_name = "larry"
        request.doctor.doctor_profile.last_name = "king"
        request.doctor.doctor_profile.specialty = Speciality()
        request.doctor.doctor_profile.specialty.specialty = "Agbo doctor"
        result = DoctorService.create_medical_report(request)
        self.assertIsNotNone(result)





