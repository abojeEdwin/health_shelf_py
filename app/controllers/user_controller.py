from bson import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient
from flask import request, jsonify, Flask
from flask import request, jsonify

from app.data.models.appointment import Appointment
from app.data.models.speciality import Speciality
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.services.Dto.appointment_request import User_Appointment_Request
from app.services.Dto.user_login_request import User_Login_Request
from app.services.user_service import UserService
from app.services.Dto.user_registration_request import User_Registration_Request


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017'
mongo = MongoClient



class User_Controller:
    UserService = UserService()


@app.route('/api/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"})
        registration_request = User_Registration_Request(
            user=User(
                user_name=data['username'],
                email=data['email'],
                pass_word=data['password'],
                user_profile=User_Profile(
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    age=data.get('age'),
                    gender=data.get('gender'),
                    phone_number=data.get('phone_number'),
                    address=data.get('address')
                )
            )
        )
        registered_user = UserService.register(registration_request)
        return jsonify({
            "status": "success",
            "user_id": str(registered_user.id),
            "username": registered_user.user_name,
            "email": registered_user.email
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/login_user', methods = ['GET'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"})
        login_request = User_Login_Request()
        login_request.email = data['email']
        login_request.password = data['password']
        login_user = UserService.login(login_request)
        return jsonify({
            "status": "success",
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/create_appointment', methods = ['POST'])
def create_appointment():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"})
        user_appointment_request = User_Appointment_Request()
        user_appointment_request.appointment = Appointment()
        user_appointment_request.appointment.patient = User()
        user_appointment_request.appointment.patient.user_name = data['username']
        user_appointment_request.appointment.patient.email = data['email']
        user_appointment_request.appointment.patient.pass_word = data['password']
        user_appointment_request.appointment.patient.user_profile = User_Profile()
        user_appointment_request.appointment.patient.user_profile.first_name = data['first_name']
        user_appointment_request.appointment.patient.user_profile.last_name = data['last_name']
        user_appointment_request.appointment.patient.user_profile.gender.value = data['gender']
        user_appointment_request.appointment.patient.user_profile.address = data['address']
        user_appointment_request.appointment.patient.user_profile.age = data['age']
        user_appointment_request.appointment.patient.user_profile.phone_number = data['phone_number']
        user_appointment_request.appointment.doctor = Doctor()
        user_appointment_request.appointment.doctor.user_name = data['username']
        user_appointment_request.appointment.doctor.email = data['email']
        user_appointment_request.appointment.doctor.password = data['password']
        user_appointment_request.appointment.doctor.doctor_profile = Doctor_Profile()
        user_appointment_request.appointment.doctor.doctor_profile.first_name = data['firstname']
        user_appointment_request.appointment.doctor.doctor_profile.last_name = data['lastname']
        user_appointment_request.appointment.doctor.doctor_profile.age = data['age']
        user_appointment_request.appointment.doctor.doctor_profile.phone_number = data['phone_number']
        user_appointment_request.appointment.doctor.doctor_profile.address = data['address']
        user_appointment_request.appointment.doctor.doctor_profile.gender = data['gender']
        user_appointment_request.appointment.doctor.doctor_profile.specialty = Speciality()
        user_appointment_request.appointment.doctor.doctor_profile.specialty.specialty =data['specialty']
        created_appointment = UserService.create_appointment(user_appointment_request)
        return jsonify({
            "status": "success",
        })
    except Exception as e:
        return jsonify({"error": str(e)})




@app.route('/api/delete_account', methods = ['DELETE'])
def delete_account():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"})
        UserService.delete_all()
        return jsonify({
            "status": "success",
        })
    except Exception as e:
        return jsonify({"error": str(e)})






if __name__ == '__main__':
    app.run(port=5000, debug=True)