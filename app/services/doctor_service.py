from typing import List

from app.data.models.appointment import Appointment
from app.data.models.medical_history import Medical_History
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.user import User
from app.data.repository.appointment_repository import AppointmentRepository
from app.data.repository.doctor_profile_repository import DoctorRepository
from app.data.repository.medical_history_repository import MedicalHistoryRepository
from app.data.repository.user_profile_repository import UserRepository
from app.exceptions.duplicate_email_exception import Duplicate_Email_Exception
from app.exceptions.duplicate_username_exception import Duplicate_Username_Exception
from app.exceptions.invalid_password_exception import Invalid_Password_Exception
from app.exceptions.user_not_found_exception import User_Not_Found_Exception
from app.services.Dto.appointment_request import User_Appointment_Request
from app.services.Dto.doctor_registration_request import Doctor_Registration_Request
from app.services.Dto.medical_history_request import Medical_History_Request
from app.services.Dto.user_login_request import User_Login_Request


class DoctorService:


    @classmethod
    def delete_all(cls):
        return DoctorRepository.delete_all()

    @classmethod
    def count(cls):
        return DoctorRepository.count_documents()

    @classmethod
    def register(cls, request : Doctor_Registration_Request)-> Doctor:
        if DoctorRepository.exists_by_email(request.doctor.email):
            raise Duplicate_Email_Exception("email already exist")
        if DoctorRepository.exists_by_username(request.doctor.user_name):
            raise Duplicate_Username_Exception("username already exist")
        doctor = Doctor()
        doctor.user_name = request.doctor.user_name
        doctor.email = request.doctor.email
        doctor.password = request.doctor.password
        doctor.doctor_profile = request.doctor.doctor_profile
        doctor.doctor_profile.specialty = request.doctor_profile.specialty
        return DoctorRepository.save(doctor)

    @classmethod
    def login(cls, doctor_login_request : User_Login_Request) -> Doctor:
        doctor_login_details = DoctorRepository.find_by_email(doctor_login_request.email)
        if not doctor_login_details:
            raise User_Not_Found_Exception("doctor not found")

        if not DoctorRepository.verify_password(doctor_login_details["password"], doctor_login_request.password):
            raise Invalid_Password_Exception("invalid password")

        return doctor_login_details

    @classmethod
    def create_appointment(cls, request: User_Appointment_Request) -> Appointment:
        patient = UserRepository.find_by_id(request.appointment.patient.id)
        doctor = DoctorRepository.find_by_id(request.appointment.doctor.id)
        return AppointmentRepository.save(request.appointment)

    @classmethod
    def find_all_appointments(cls) -> List[Appointment]:
        result = AppointmentRepository.find_all()
        return result

    @classmethod
    def count_documents(cls):
        return DoctorRepository.count_documents()

    @classmethod
    def find_all(cls) -> List[Doctor]:
        return DoctorRepository.find_all()

    @classmethod
    def delete_by_id(cls, id):
        return DoctorRepository.delete_by_id(id)

    @classmethod
    def create_medical_report(cls, request: Medical_History_Request):
        if not hasattr(request.patient, 'id') or not request.patient.id:
            request.patient = UserRepository.save(request.patient)
        if not hasattr(request.doctor, 'id') or not request.doctor.id:
            request.doctor = DoctorRepository.save(request.doctor)
        medical_record = Medical_History(
            patient=request.patient,
            doctor=request.doctor,
            medical_history_details=request.medical_history.medical_history_details
        )

        return MedicalHistoryRepository.save(medical_record)