from infrasctructure.adapters.googlesheet_adapter import GoogleSheetAdapter
from infrasctructure.adapters.database_adapter import DatabaseAdapter
from domain.repositories.AnalisysRepository import AnalisysRepository
from domain.repositories.EquipmentRepository import EquipmentRepository
from domain.repositories.ParameterRepository import ParameterRepository

def get_equipament_data_googlesheet():
    from main import app
    sheet_name = 'Equipamento'
    gc_adapter = GoogleSheetAdapter(app.config['CREDENTIALS_GOOGLE_SHEET'], app.config['SHEET_ID'])
    equipment_repository = EquipmentRepository(gc_adapter.connect_sheets(),sheet_name=sheet_name )
    return equipment_repository.work_sheet().get_all_records()

def get_equipment_data_database():
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    equipment_repository = EquipmentRepository(database_adapter=database_adapter)
    return equipment_repository.get_equipment()

def get_analisys_data_googlesheet():
    from main import app
    sheet_name = 'Analise'
    gc_adapter = GoogleSheetAdapter(app.config['CREDENTIALS_GOOGLE_SHEET'], app.config['SHEET_ID'])
    analisys_repository = AnalisysRepository(gc_adapter.connect_sheets(), sheet_name)
    return analisys_repository.work_sheet().get_all_records()

def get_analisys_data_database():
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    analisys_repository = AnalisysRepository(database_adapter=database_adapter)
    return analisys_repository.get_analisys()

def get_analisys_from_equipmentAndParameter_database():
    
    from main import app        
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    analisys_repository = AnalisysRepository(database_adapter=database_adapter)
    return analisys_repository.get_analisys_by_equipment_parameter()

def get_parameter_data_googlesheet():
    from main import app
    sheet_name = 'Parametro'
    gc_adapter = GoogleSheetAdapter(app.config['CREDENTIALS_GOOGLE_SHEET'], app.config['SHEET_ID'])    
    parameter_repository = ParameterRepository(gc_adapter.connect_sheets(), sheet_name)
    return parameter_repository.work_sheet().get_all_records()

def get_parameter_data_database():
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    parameter_repository = ParameterRepository(database_adapter=database_adapter)
    return parameter_repository.get_parameter()    
    
def migration_from_google_sheet_to_database():
   
    try:
        #insert_equipament_data(get_equipament_data_googlesheet())    
        #insert_parameter_data(get_parameter_data_googlesheet())
        #insert_analisys_data(get_analisys_data_googlesheet())
        update_analisys_data(get_analisys_data_googlesheet())
        update_parameter_data(get_parameter_data_googlesheet())
        update_equipment_data(get_equipament_data_googlesheet())
        return True
    except Exception as e:
        raise e
    
    
def insert_equipament_data(data):
    print('data',data)
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    status=EquipmentRepository(database_adapter=database_adapter).insert_equipment(data)
    return status

def insert_parameter_data(data):
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    status=ParameterRepository(database_adapter=database_adapter).insert_parameter(data)
    return status

def insert_analisys_data(data):
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    status=AnalisysRepository(database_adapter=database_adapter).insert_analisys(data)
    return status

def update_equipment_data(data):
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    status=EquipmentRepository(database_adapter=database_adapter).update_equipment(data)
    return status

def update_parameter_data(data):
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    status=ParameterRepository(database_adapter=database_adapter).update_parameter(data)
    return status

def update_analisys_data(data):
    from main import app    
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_adapter = DatabaseAdapter(database_uri)
    status=AnalisysRepository(database_adapter=database_adapter).update_analisys(data)
    return status
    