from typing import Union, List, Optional
from bson import ObjectId
from app.data.models.appointment import Appointment
from app.data.models.users import user
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.data.repository.appointment_repository import AppointmentRepository
from app.data.repository.user_profile_repository import UserRepository
from app.data.repository.doctor_profile_repository import DoctorRepository
from app.data.repository.medical_history_repository import MedicalHistoryRepository
from app.exceptions.duplicate_email_exception import Duplicate_Email_Exception
from app.exceptions.duplicate_username_exception import Duplicate_Username_Exception
from app.exceptions.invalid_password_exception import Invalid_Password_Exception
from app.services.Dto.appointment_request import User_Appointment_Request
from app.services.Dto.user_login_request import User_Login_Request
from app.services.Dto.user_registration_request import User_Registration_Request
from app.exceptions.user_not_found_exception import User_Not_Found_Exception


class UserService:

    UserRepository = UserRepository
    AppointmentRepository = AppointmentRepository
    DoctorRepository= DoctorRepository
    MedicalHistoryRepository = MedicalHistoryRepository


    @classmethod
    def count(cls):
        return UserRepository.count_documents()

    @classmethod
    def delete_all(cls):
        return UserRepository.delete_all()

    @classmethod
    def find_by_id(cls, id)-> bool:
        return UserRepository.exists_by_id(id)

    @classmethod
    def find_all(cls)-> List[User]:
        return UserRepository.find_all()

    @classmethod
    def delete_by_id(cls, id):
        return UserRepository.delete_by_id(id)

    @classmethod
    def register(cls, request : User_Registration_Request) -> User:

        if UserRepository.exists_by_username(request.user.user_name):
            raise Duplicate_Username_Exception("username already exist")

        if UserRepository.exist_by_email(request.user.email):
            raise Duplicate_Email_Exception("email already exist")

        if not request.user.pass_word:
            raise ValueError("Password is required")
        user = User()
        user.user_name = request.user.user_name
        user.email = request.user.email
        user.pass_word = request.user.pass_word
        user.user_profile = request.user.user_profile
        return UserRepository.save(user)

    @classmethod
    def login(cls, login_request : User_Login_Request) -> User:
            user_login_details = UserRepository.find_by_email(login_request.email)
            if not user_login_details:
                raise User_Not_Found_Exception("user not found")
            if not UserRepository.verify_password(user_login_details["password"],login_request.password):
                raise Invalid_Password_Exception("invalid password")

            return user_login_details

    @classmethod
    def create_appointment(cls, request : User_Appointment_Request) -> Appointment:
        patient = UserRepository.find_by_id(request.appointment.patient.id)
        doctor = DoctorRepository.find_by_id(request.appointment.doctor.id)
        return AppointmentRepository.save(request.appointment)

    @classmethod 
    def find_all_appointments(cls)-> List[Appointment]:
        result = AppointmentRepository.find_all()
        return result

    @classmethod
    def get_appointment(cls,appointment_id: Union[str, ObjectId]) -> Optional[Appointment]:
        return AppointmentRepository.get_appointment_by_id(appointment_id)
