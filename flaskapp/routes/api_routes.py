# api_routes.py
from flask import Blueprint, request, jsonify
from models import MachineData, db
from datetime import datetime

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/machine_data', methods=['POST'])
def add_machine_data():
    try:
        data = request.json
        new_data = MachineData(
            machine_id=data.get('machine_id'),
            temperature=data.get('temperature')
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"msg": "Data added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_blueprint.route('/machine_data', methods=['GET'])
def get_machine_data():
    try:
        data = MachineData.query.all()
        result = [{"machine_id": item.machine_id, "temperature": item.temperature, "timestamp": item.timestamp} for item in data]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
