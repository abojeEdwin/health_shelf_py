import unittest
import pytest

from app.data.models.gender import Gender
from app.data.models.medical_history import Medical_History
from app.data.models.speciality import Speciality
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.data.repository.medical_history_repository import MedicalHistoryRepository
from migrations.medical_history_database import db

@pytest.mark.mongodb
class TestMedicalHistoryRepository(unittest.TestCase):
    MedicalHistoryRepository = MedicalHistoryRepository

    def setUp(self):
        db.medical_history.delete_many({})

    def tearDown(self):
        db.medical_history.delete_many({})


    def test_create_and_save_medical_history(self):
        assert MedicalHistoryRepository.count_documents() == 0
        medical_history = Medical_History()
        medical_history.patient = User()
        medical_history.medical_history_details = "Your medical history details"
        medical_history.patient.user_name = "user_name"
        medical_history.patient.pass_word = "pass_word"
        medical_history.patient.email = "email@example.com"
        medical_history.patient.user_profile = User_Profile()
        medical_history.patient.user_profile.first_name = "first_name"
        medical_history.patient.user_profile.last_name = "last_name"
        medical_history.patient.user_profile.gender = Gender.MALE
        medical_history.patient.user_profile.address = "Abuja"
        medical_history.patient.user_profile.age = "79"
        medical_history.patient.user_profile.phone_number = "+23477665532"
        medical_history.doctor = Doctor()
        medical_history.doctor.user_name = "doc kiriku"
        medical_history.doctor.password = "password"
        medical_history.doctor.email = "doc@example.com"
        medical_history.doctor.doctor_profile = Doctor_Profile()
        medical_history.doctor.doctor_profile.phone_number = "+23477665532"
        medical_history.doctor.doctor_profile.gender = Gender.MALE
        medical_history.doctor.doctor_profile.address = "Abuja"
        medical_history.doctor.doctor_profile.age = "60"
        medical_history.doctor.doctor_profile.first_name = "larry"
        medical_history.doctor.doctor_profile.last_name = "king"
        medical_history.doctor.doctor_profile.specialty = Speciality()
        medical_history.doctor.doctor_profile.specialty.specialty = "Agbo doctor"
        result = MedicalHistoryRepository.save(medical_history)
        assert result.id is not None


    def test_update_medical_history(self):

            medical_history = Medical_History()
            medical_history.medical_history_details = "You have Corona Virus"
            medical_history.patient = User()
            medical_history.patient.user_name = "user_name"
            medical_history.patient.pass_word = "pass_word"
            medical_history.patient.email = "email@example.com"
            medical_history.patient.user_profile = User_Profile()
            medical_history.patient.user_profile.first_name = "first_name"
            medical_history.patient.user_profile.last_name = "last_name"
            medical_history.patient.user_profile.gender = Gender.MALE
            medical_history.patient.user_profile.address = "Abuja"
            medical_history.patient.user_profile.age = "79"
            medical_history.patient.user_profile.phone_number = "+23477665532"
            medical_history.doctor = Doctor()
            medical_history.doctor.user_name = "doc_kiriku"
            medical_history.doctor.password = "password"
            medical_history.doctor.email = "doc@example.com"
            medical_history.doctor.doctor_profile = Doctor_Profile()
            medical_history.doctor.doctor_profile.phone_number = "+23477665532"
            medical_history.doctor.doctor_profile.gender = Gender.MALE
            medical_history.doctor.doctor_profile.address = "Abuja"
            medical_history.doctor.doctor_profile.age = "60"
            medical_history.doctor.doctor_profile.first_name = "larry"
            medical_history.doctor.doctor_profile.last_name = "king"
            medical_history.doctor.doctor_profile.specialty = Speciality()
            medical_history.doctor.doctor_profile.specialty.specialty = "Agbo doctor"
            saved_history = MedicalHistoryRepository.save(medical_history)
            assert saved_history.id is not None
            assert MedicalHistoryRepository.count_documents() == 1

            medical_history.medical_history_details = "now na COVID-19 you get"
            medical_history.patient.user_profile.phone_number = "+23477777777"
            medical_history.doctor.doctor_profile.specialty.specialty = "COVID Specialist"
            update_success = MedicalHistoryRepository.update(medical_history, saved_history.id)
            assert MedicalHistoryRepository.count_documents() == 1
            updated_history = MedicalHistoryRepository.find_by_id(saved_history.id)
            assert updated_history is not None





