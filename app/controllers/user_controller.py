from pymongo import MongoClient
from flask import request, jsonify, Flask
from flask import request, jsonify
from app.data.models.appointment import Appointment
from app.data.models.gender import Gender
from app.data.models.medical_history import Medical_History
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
from app.exceptions.duplicate_email_exception import Duplicate_Email_Exception
from app.services.Dto.appointment_request import User_Appointment_Request
from app.services.Dto.medical_history_request import Medical_History_Request
from app.services.Dto.user_login_request import User_Login_Request
from app.services.user_service import UserService
from app.services.Dto.user_registration_request import User_Registration_Request
from app.exceptions.duplicate_username_exception import Duplicate_Username_Exception

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

@app.route('/api/login', methods = ['GET'])
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

@app.route('/api/create_appointment', methods = ['GET'])
def create_appointment():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Request body must be JSON"})
            appointment_request = User_Appointment_Request(
                appointment=Appointment(
                    appointment=User(id=data['patient_id']),
                    doctor=Doctor(id=data['doctor_id']),
                )
            )
            appointment = UserService.create_appointment(appointment_request)
            return jsonify({
                "status": "success",
            })
        except Exception as e:
            return jsonify({"error": str(e)})








if __name__ == '__main__':
    app.run(port=5006, debug=True)