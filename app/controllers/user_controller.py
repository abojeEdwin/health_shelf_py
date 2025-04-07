from bson import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient
from flask import request, jsonify, Flask
from flask import request, jsonify
from app.data.models.users.user import User
from app.data.models.users.user_profile import User_Profile
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

@app.route('/api/create_appointment', methods = ['GET'])
def create_appointment():
    pass

@app.route('/api/delete_account', methods = ['DELETE'])
def delete_account(user_id):
        pass




if __name__ == '__main__':
    app.run(port=5006, debug=True)