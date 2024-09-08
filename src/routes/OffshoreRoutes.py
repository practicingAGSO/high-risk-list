from flask import Blueprint, jsonify, request
from src.services.OffshoreService import get_data_from_offshore_leaks
from src.utils.Limiter import limiter
from flask_jwt_extended import jwt_required


offshore_bp = Blueprint('offshore', __name__)

@offshore_bp.route('/offshore_leaks', methods=['GET'])
@limiter.limit("20 per minute", override_defaults=False)
@jwt_required()
def get_offshore_leaks():
    name = request.args.get('name')

    if not name:
        return jsonify({"error": "El parámetro 'name' es requerido."}), 400

    data = get_data_from_offshore_leaks(name).to_dict()

    
    return jsonify(data), 200