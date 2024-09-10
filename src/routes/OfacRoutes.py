from flask import Blueprint, jsonify, request
from src.services.OfacService import get_data_from_sanctions_list
from src.utils.Limiter import limiter
from flask_jwt_extended import jwt_required

ofac_bp = Blueprint('ofac', __name__)

@ofac_bp.route('/ofac_sanctions_list', methods=['GET'])
@limiter.limit("20 per minute", error_message="Request limit reached. Wait a moment to use again.")
@jwt_required()
def get_ofac_sanctions_list():
    name = request.args.get('name')

    if not name:
        return jsonify({"error": "The parameter 'name' is required."}), 400

    data = get_data_from_sanctions_list(name).to_dict()

    
    return jsonify(data), 200