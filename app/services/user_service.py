from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.data.repository.appointment_repository import AppointmentRepository
from app.data.repository.user_profile_repository import UserRepository
from app.data.repository.doctor_profile_repository import DoctorRepository
from app.data.repository.medical_history_repository import MedicalHistoryRepository
from app.services.Dto.user_registration_request import User_Registration_Request


class UserService:

    UserRepository = UserRepository
    AppointmentRepository = AppointmentRepository
    DoctorRepository= DoctorRepository
    MedicalHistoryRepository = MedicalHistoryRepository

    @classmethod
    def register(cls, request : User_Registration_Request) -> User:
        if not request.user.pass_word:
            raise ValueError("Password is required")
        user = User()
        user.user_name = request.user.user_name
        user.email = request.user.email
        user.pass_word = request.user.pass_word
        user.user_profile = request.user.user_profile
        return UserRepository.save(user)

    @classmethod
    def count(cls):
        return UserRepository.count_documents()

    @classmethod
    def delete_all(cls):
        return UserRepository.delete_all()
