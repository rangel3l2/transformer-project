import gspread as gc
from infrasctructure.database.models import Analisys
from infrasctructure.adapters.Base import Base
import pymysql
from sqlalchemy import exc
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
                    analisys = Analisys(id_analisys=item['idAnalise'], enter_date=item['dataEntrada'], sampling_date=item['dataAnalise'], status=item['status'], serie_id=item['serieid'], id_parameter=item['idParametro'])
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
    
    
    