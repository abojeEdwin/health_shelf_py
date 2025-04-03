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
        db.appointments.delete_many({})

    def tearDown(self):
        db.appointments.delete_many({})

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
        appointment.doctor.user_name = "masha"
        appointment.doctor.password = "password"
        appointment.doctor.email = "jagaga@gmail.com"
        appointment.doctor.doctor_profile = Doctor_Profile()
        appointment.doctor.doctor_profile.first_name = "doctor injection"
        appointment.doctor.doctor_profile.last_name = "you no go cry ke?"
        appointment.doctor.doctor_profile.age = "200"
        appointment.doctor.doctor_profile.specialty = "Agbo doctor"
        appointment.doctor.doctor_profile.phone_number = "+2348899023"
        appointment.doctor.doctor_profile.address = "Abuja"
        appointment.doctor.doctor_profile.gender = Gender.MALE
        appointment.appointment_details = " You have Corona Virus"
        AppointmentRepository.save(appointment)
        assert AppointmentRepository.count_documents() == 1


    def test_delete_appointment(self):
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
        AppointmentRepository.delete_appointment(appointment)
        assert AppointmentRepository.count_documents() == 0

    def test_update_appointment(self):
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
        appointment1 = Appointment()
        appointment1.patient = User()
        appointment1.patient.first_name = "mandaline"
        appointment1.patient.last_name = "bunawewo"
        appointment1.patient.pass_word = "password007"
        appointment1.patient.email = "trojanhorse@gmail.com"
        appointment1.patient.user_profile = User_Profile()
        appointment1.patient.user_profile.first_name = "malik"
        appointment1.patient.user_profile.gender = Gender.FEMALE
        appointment1.patient.user_profile.address = "London, Cardiff"
        appointment1.doctor = Doctor()
        appointment1.doctor.first_name = "doctor salt"
        appointment1.doctor.last_name = "light"
        appointment1.doctor.user_name = "mashalee"
        appointment1.doctor.password = "passjerk"
        appointment1.doctor.email = "jagfarm@gmail.com"
        appointment1.doctor.doctor_profile = Doctor_Profile()
        appointment1.doctor.doctor_profile.age = "23"
        appointment1.doctor.doctor_profile.specialty = "Agbo doctor"
        appointment1.doctor.doctor_profile.phone_number = "+2348899023"
        appointment1.doctor.doctor_profile.address = "Lagos"
        appointment1.doctor.doctor_profile.gender = Gender.MALE
        appointment1.appointment_details = " You need to treat malaria"
        result = AppointmentRepository.update(appointment1)
        assert AppointmentRepository.count_documents() == 1


    def test_find_appointments_by_id(self):
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
        appointment.doctor.user_name = "masha"
        appointment.doctor.password = "password"
        appointment.doctor.email = "jagaga@gmail.com"
        appointment.doctor.doctor_profile = Doctor_Profile()
        appointment.doctor.doctor_profile.first_name = "doctor injection"
        appointment.doctor.doctor_profile.last_name = "you no go cry ke?"
        appointment.doctor.doctor_profile.age = "200"
        appointment.doctor.doctor_profile.specialty = "Agbo doctor"
        appointment.doctor.doctor_profile.phone_number = "+2348899023"
        appointment.doctor.doctor_profile.address = "Abuja"
        appointment.doctor.doctor_profile.gender = Gender.MALE
        appointment.appointment_details = " You have Corona Virus"
        AppointmentRepository.save(appointment)
        assert AppointmentRepository.count_documents() == 1
        found_id = AppointmentRepository.find_by_id(appointment.id)
        assert found_id.id is not None


