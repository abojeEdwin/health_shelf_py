from flask import Flask, jsonify, request
from pymongo import MongoClient
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from app.exceptions.duplicate_email_exception import Duplicate_Email_Exception
from app.exceptions.duplicate_username_exception import Duplicate_Username_Exception
from app.services.Dto.doctor_registration_request import Doctor_Registration_Request
from app.services.doctor_service import DoctorService


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017'
mongo = MongoClient



class Doctor_Controller:
    DoctorService = DoctorService()


@app.route('/api/register_doctor', methods=['POST'])
def register_doctor():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}),
        doctor_profile = Doctor_Profile(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=data.get('age'),
            gender=data.get('gender'),
            phone_number=data.get('phone_number'),
            address=data.get('address'),
            specialty=data['specialty'] )
        doctor = Doctor(
            user_name=data['username'],
            email=data['email'],
            password=data['password'],
            doctor_profile=doctor_profile)
        registration_request = Doctor_Registration_Request(doctor=doctor)
        registered_doctor = DoctorService.register(registration_request)
        return jsonify({
            "status": "success",
        })
    except Duplicate_Email_Exception as e:
        return jsonify({"error": str(e)})
    except Duplicate_Username_Exception as e:
        return jsonify({"error": str(e)})
    except Exception as e:
        return jsonify({"error": str(e)})







if __name__ == '__main__':
    app.run(port=5009, debug=True)