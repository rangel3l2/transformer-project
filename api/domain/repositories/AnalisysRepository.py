import gspread as gc
from infrasctructure.database.models import Analisys
from infrasctructure.adapters.Base import Base
import pymysql
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import exc, text
from infrasctructure.database.models import Analisys, Parameter, Equipment, ChemicalAnalized
import json
from datetime import datetime, timezone, date
class AnalisysRepository:
    def __init__(self, connected_sheets=None, sheet_name=None, database_adapter =None):
        self.connected_sheets = connected_sheets
        self.sheet_name = sheet_name
        self.database_adapter = database_adapter
    def work_sheet(self):
        return self.connected_sheets.worksheet(self.sheet_name)
    
    def insert_analisys(self, analisys):
        try:
            session = self.database_adapter.get_session()
            
            Base.metadata.tables['Analise'].create(self.database_adapter.engine, checkfirst=True)
            
            for item in analisys:
                
                existing_entry = session.query(Analisys).filter_by(id_analisys=item['idAnalise']).first()
                if not existing_entry:
                    
                    analisys = Analisys(id_analisys=item['idAnalise'], enter_date=self.get_formatted_date(), sampling_date=item['dataAnalise'], status=item['status'], serie_id=item['serieid'], id_parameter=item['idParametro'])
                    session.add(analisys)
                    
                try:
                 session.commit()
                except pymysql.err.IntegrityError as e:
                    session.rollback()
                except exc.IntegrityError as e:
                    session.rollback()
                except Exception as e:
                    session.rollback()
            session.close()
            return True
        except Exception as e:
            raise e
        
    def update_analisys(self, analisys):
        try:
            session = self.database_adapter.get_session()
            for item in analisys:
                existing_entry = session.query(Analisys).filter_by(id_analisys=item['idAnalise']).first()
                
                if existing_entry:
                    # Atualizar apenas os campos que são diferentes
                    updated = False
                    if existing_entry.enter_date != self.get_formatted_date():
                        existing_entry.enter_date = self.get_formatted_date()
                        updated = True
                    if existing_entry.sampling_date != item['dataAnalise']:
                        existing_entry.sampling_date = item['dataAnalise']
                        updated = True
                    if existing_entry.status != item['status']:
                        existing_entry.status = item['status']
                        updated = True
                    if existing_entry.serie_id != item['serieid']:
                        existing_entry.serie_id = item['serieid']
                        updated = True
                    if existing_entry.id_parameter != item['idParametro']:
                        existing_entry.id_parameter = item['idParametro']
                        updated = True
                    
                    if updated:
                        session.commit()

            session.close()
            return True
        except Exception as e:
            session.rollback()
            raise e



    def get_analisys(self):
        try:
            session = self.database_adapter.get_session()
            analisys = session.query(Analisys).all()
            session.close()
            for item in analisys:
                
                if hasattr(item, '_sa_instance_state'):
                    item.__dict__.pop('_sa_instance_state')
                    
            #transformar analisys em dict
            
            analisys = [item.__dict__ for item in analisys]      
            return analisys
        except Exception as e:
            raise e
    
    def get_analisys_by_equipment_parameter(self):
        try:
            session = self.database_adapter.get_session()
            analisys = session.query(
                    Analisys,
                    Parameter,
                    Equipment,
                    ChemicalAnalized
            ).join(Parameter, Analisys.id_parameter == Parameter.id_parameter).join(Equipment, Parameter.id_parameter == Equipment.serie_id).join(ChemicalAnalized, Analisys.id_chemical_analized == ChemicalAnalized.id_chemical_analized).all()
            session.close()
            result_list = []
            result_dict = []
            for analise, parametro, equipamento, chemical in analisys:
              result_dict.append( {
                    'analysis': self.to_dict(analise),
                    'parameter': self.to_dict(parametro),
                    'equipment': self.to_dict(equipamento),
                    'chemical': self.to_dict(chemical)
              } )
              result_list.append(result_dict)    
            return result_dict
           
        except Exception as e:
            raise e
    
    def to_dict(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, (datetime, date)):
                        fields[field] = data.isoformat()  # Serialize datetime/date to ISO format
                    else:
                        json.dumps(data)  # Check if the field can be serialized to JSON
                        fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return None
    
    def get_formatted_date(self):
        now = datetime.now(timezone.utc).now()  
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        return formatted_date
            
