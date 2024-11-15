# routes/auth_routes.py
from flask import Blueprint, jsonify, request

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    # ตัวอย่างโค้ดสำหรับการล็อกอิน
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # ตรวจสอบข้อมูลการล็อกอินที่นี่
    if username == "admin" and password == "admin":
        return jsonify({"msg": "Login successful"}), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401
