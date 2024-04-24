import gspread as gc
from infrasctructure.database.models import Equipment
from infrasctructure.adapters.Base import Base
class EquipmentRepository:
    def __init__(self, connected_sheets=None, sheet_name=None, database_adapter =None):
        self.connected_sheets = connected_sheets
        self.sheet_name = sheet_name
        self.database_adapter = database_adapter
    def work_sheet(self):
        return self.connected_sheets.worksheet(self.sheet_name)
    
    def insert_equipment(self, equipment):
        
        try:
            session = self.database_adapter.get_session()
            Base.metadata.tables['Equipamento'].create(self.database_adapter.engine, checkfirst=True)

            for item in equipment:
                existing_entry = session.query(Equipment).filter_by(serie_id=item['serieid']).first()
                if not existing_entry:
                    equipment = Equipment(serie_id=item['serieid'], owner=item['proprietario'], tag=item['tag'], place_installed=item['localInstalação'], manufacturer=item['fabricante'], year_of_manufacture=item['anoFabricação'], tension_primary=item['tensaoPrimaria'], tension_secondary=item['tensaoSecundaria'], max_power=item['maxPotencia'], volume_of_oil=item['volumeOleo'], sampling_address=item['enderecoAmostragem'])
                    session.add(equipment)
                    session.commit()
            session.close()
            return True
        except Exception as e:
            raise e
    def get_equipment(self):
        try:
            session = self.database_adapter.get_session()
            equipment = session.query(Equipment).all()
            session.close()
            if not equipment:
                return None
            for item in equipment:
                if hasattr(item, '_sa_instance_state'):
                    item.__dict__.pop('_sa_instance_state')
                    
            #transformar equipment em dict
            
            equipment = [item.__dict__ for item in equipment]        

            return equipment
        except Exception as e:
            raise e
    
        