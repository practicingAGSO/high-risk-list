from flask import Blueprint, jsonify, request
from src.services.UserService import UserService
from src.services.UserService import UserService


user_bp = Blueprint('auth', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = UserService().register(username, password)
    return jsonify({"message": "User registered successfully", "user": user.__dict__}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    result = UserService().login(username, password)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
    