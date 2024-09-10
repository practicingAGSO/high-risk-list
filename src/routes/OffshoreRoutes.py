from flask import Blueprint, jsonify, request
from src.services.OffshoreService import get_data_from_offshore_leaks
from src.utils.Limiter import limiter
from flask_jwt_extended import jwt_required


offshore_bp = Blueprint('offshore', __name__)

@offshore_bp.route('/offshore_leaks', methods=['GET'])
@limiter.limit("20 per minute", error_message="Request limit reached. Wait a moment to use again.")
@jwt_required()
def get_offshore_leaks():
    name = request.args.get('name')

    if not name:
        return jsonify({"error": "The parameter 'name' is required"}), 400

    data = get_data_from_offshore_leaks(name).to_dict()

    
    return jsonify(data), 200