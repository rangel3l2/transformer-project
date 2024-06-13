from flask import Blueprint, jsonify, request
from application.use_cases import get_equipament_data_googlesheet, get_parameter_data_googlesheet, get_analisys_data_googlesheet, get_equipment_data_database, get_analisys_data_database, get_parameter_data_database, get_analisys_from_equipmentAndParameter_database
from application.durval_triangle_use_cases import generate_durval_triangle
from domain.entities import Analisys, Parameter, Equipment
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')
@api_blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bem-vindo ao sistema de gerenciamento de tranformador!'})

@api_blueprint.route('/googlesheet/equipment', methods=['GET'])
def get_equipament_googlesheet():    
    return jsonify(get_equipament_data_googlesheet())

@api_blueprint.route('/googlesheet/analisys', methods=['GET'])
def get_analisys_googlesheet():    
    return jsonify(get_analisys_data_googlesheet())

@api_blueprint.route('/googlesheet/parameter', methods=['GET'])
def get_parameter_googlesheet():    
    return jsonify(get_parameter_data_googlesheet())

@api_blueprint.route('/migrate', methods=['POST'])
def migrate():
    from application.use_cases import migration_from_google_sheet_to_database
    status = migration_from_google_sheet_to_database()
    return jsonify({'status': status})

@api_blueprint.route('/equipment', methods=['GET'])
def get_equipment():
    #transforme data to equipment model
    
   
    return jsonify(get_equipment_data_database())

@api_blueprint.route('/analisys', methods=['GET'])
def get_analisys():
   
    return jsonify(get_analisys_from_equipmentAndParameter_database())

@api_blueprint.route('/parameter', methods=['GET'])
def get_parameter():
    
    return jsonify(get_parameter_data_database())

@api_blueprint.route('/durval_triangle', methods=['GET'])
def get_durval_triangle():
    analisys = get_analisys_from_equipmentAndParameter_database()
    return jsonify(generate_durval_triangle(analisys))