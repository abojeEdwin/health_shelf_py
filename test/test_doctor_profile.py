import unittest
import pytest

from app.data.models.gender import Gender
from app.data.models.speciality import Speciality
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.repository.doctor_profile_repository import DoctorRepository
from migrations.doctor_data_base import db


@pytest.mark.mongodb
class TestDoctorProfileRepository(unittest.TestCase):

    DoctorProfileRepository = DoctorRepository
    def setUp(self):
        db.doctors.delete_many({})

    def tearDown(self):
        db.doctors.delete_many({})


    def test_save_doctor_profile(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        result = DoctorRepository.save(doctor)
        assert result.id is not None

    def test_delete_doctor_profile(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        DoctorRepository.delete(doctor)
        assert DoctorRepository.count_documents() == 0


    def test_doctor_update_doctor_profile(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        DoctorRepository.update(doctor, doctor.id)
        assert DoctorRepository.count_documents() == 1

    def test_find_doctor_by_email(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        self.assertTrue(DoctorRepository.exists_by_email("docjegz@gmail.com"))

    def test_find_doctor_by_username(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        self.assertTrue(DoctorRepository.exists_by_username("jegz"))



    def test_find_doctor_by_user_name(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        result = DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        DoctorRepository.find_by_username("jegz")
        assert result.id is not None


    def test_doctor_exists_by_id(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        result = DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        self.assertTrue(DoctorRepository.exists_by_id(doctor.id))

    def test_delete_doctor_by_id(self):
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.age = "1100"
        doctor.doctor_profile.phone_number = "+24309890965356"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Agbo Doctor"
        DoctorRepository.save(doctor)
        assert DoctorRepository.count_documents() == 1
        self.assertTrue(DoctorRepository.delete_by_id(doctor.id))


    def test_delete_doctors_by_id(self):
        users_ids = []
        assert DoctorRepository.count_documents() == 0
        doctor = Doctor()
        doctor.email = "docjegz@gmail.com"
        doctor.password = "password"
        doctor.user_name = "jegz"
        doctor.doctor_profile = Doctor_Profile()
        doctor.doctor_profile.gender = Gender.FEMALE
        doctor.doctor_profile.first_name = "John"
        doctor.doctor_profile.last_name = "Doe"
        doctor.doctor_profile.address = "Congo"
        doctor.doctor_profile.specialty = Speciality()
        doctor.doctor_profile.specialty.specialty = "Optician"
        DoctorRepository.save(doctor)
        users_ids.append(doctor.id)

        doctor1 = Doctor()
        doctor1.email = "docjegz@gmail.com"
        doctor1.password = "password"
        doctor1.user_name = "jegz"
        doctor1.doctor_profile = Doctor_Profile()
        doctor1.doctor_profile.gender = Gender.FEMALE
        doctor1.doctor_profile.first_name = "John"
        doctor1.doctor_profile.last_name = "Doe"
        doctor1.doctor_profile.address = "Congo"
        doctor1.doctor_profile.specialty = Speciality()
        doctor1.doctor_profile.specialty.specialty = "Agbo Doctor"
        DoctorRepository.save(doctor1)
        users_ids.append(doctor1.id)

        assert DoctorRepository.count_documents() == 2
        DoctorRepository.delete_doctors_by_id(users_ids)
        assert DoctorRepository.count_documents() == 0







