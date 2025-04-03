import unittest
from datetime import datetime

import pytest

from app.data.models.gender import Gender
from app.data.models.users.doctors import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from migrations.appointment_database import db
from app.data.repository.appointment_repository import AppointmentRepository
from app.data.models.appointment import Appointment


@pytest.mark.mongodb
class TestAppointmentRepository(unittest.TestCase):

    AppointmentRepository = AppointmentRepository

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_and_save_appointment(self):
        appointment = Appointment()
        appointment.patient = User()
        appointment.patient.first_name = "dele"
        appointment.patient.last_name = "kasongo"
        appointment.patient.pass_word = "password"
        appointment.patient.email = "trojan@gmail.com"
        appointment.patient.user_profile = User_Profile()
        appointment.patient.user_profile.first_name = "dele"
        appointment.patient.user_profile.gender = Gender.FEMALE
        appointment.patient.user_profile.address = "London, UK"
        appointment.doctor = Doctor()
        appointment.doctor.first_name = "doctor injection"
        appointment.doctor.last_name = "you no go cry ke?"
        appointment.doctor.user_name = "masha"
        appointment.doctor.password = "password"
        appointment.doctor.email = "jagaga@gmail.com"
        appointment.doctor.doctor_profile = Doctor_Profile()
        appointment.doctor.doctor_profile.age = "200"
        appointment.doctor.doctor_profile.specialty = "Agbo doctor"
        appointment.doctor.doctor_profile.phone_number = "+2348899023"
        appointment.doctor.doctor_profile.address = "Abuja"
        appointment.doctor.doctor_profile.gender = Gender.MALE
        appointment.appointment_details = " You have Corona Virus"
        appointment.local_time = datetime.now()
        AppointmentRepository.save(appointment)
        assert AppointmentRepository.count_documents() == 1




