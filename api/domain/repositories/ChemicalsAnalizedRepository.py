
import gspread as gc
from infrasctructure.database.models import ChemicalAnalized
from infrasctructure.adapters.Base import Base

class ChemicalsAnalizedRepository:
    def __init__ (self, connected_sheets=None, sheet_name=None, database_adapter=None):
        self.connected_sheets = connected_sheets
        self.sheet_name = sheet_name
        self.database_adapter = database_adapter
    
    def work_sheet(self):
        return self.connected_sheets.worksheet(self.sheet_name)
    
    def get_chemicals_analized(self):
        try:
            session = self.database_adapter.get_session()
            chemicals_analized = session.query(ChemicalAnalized).all()
            session.close()
            for item in chemicals_analized:
                if item:
                    item = item.__dict__
                    item.pop('_sa_instance_state')
            chemicals_analized = [item.__dict__ for item in chemicals_analized]
            if not chemicals_analized:
                return None
            return chemicals_analized
        except Exception as e:
            raise e
        
    def insert_chemicals_analized(self, chemicals_analized):
        try:
            session = self.database_adapter.get_session()
            Base.metadata.tables['QuimicosAnalisados'].create(self.database_adapter.engine, checkfirst=True)
            
            for item in chemicals_analized:
                print(item)
                existing_entry = session.query(ChemicalAnalized).filter_by(id_chemical_analized=item['id_quimicos_analisados']).first()
                if not existing_entry:
                    chemical_analized = ChemicalAnalized(id_chemical_analized=item['id_quimicos_analisados'], hidrogen = item['hidrogenio'], oxygen = item['oxigenio'], nitrogen = item['nitrogenio'], carbon_monoxide = item['monoxido_carbono'], methane = item['metano'], carbon_dioxide = item['dioxido_carbono'], ethylene = item['etileno'], ethane = item['etano'], acetylene = item['acetileno'], co2_co_ratio = item['razao_co2_co'], total_combustible_gases = item['total_gases_combustiveis'], total_gases = item['total_gases'])
                    session.add(chemical_analized)
                    session.commit()
            session.close()
            return True
        except Exception as e:
            raise e
        
    def update_chemicals_analized(self, chemicals_analized):
        try:
            session = self.database_adapter.get_session()
            for item in chemicals_analized:
                existing_entry = session.query(ChemicalAnalized).filter_by(id_chemical_analized=item['id_quimicos_analisados']).first()
                if existing_entry is not None:
                    updated = False
                    if existing_entry.hidrogen != item['hidrogenio']:
                        existing_entry.hidrogen = item['hidrogenio']
                        updated = True
                    if existing_entry.oxygen != item['oxigenio']:
                        existing_entry.oxygen = item['oxigenio']
                        updated = True
                    if existing_entry.nitrogen != item['nitrogenio']:
                        existing_entry.nitrogen = item['nitrogenio']
                        updated = True
                    if existing_entry.carbon_monoxide != item['monoxido_carbono']:
                        existing_entry.carbon_monoxide = item['monoxido_carbono']
                        updated = True
                    if existing_entry.methane != item['metano']:
                        existing_entry.methane = item['metano']
                        updated = True
                    if existing_entry.carbon_dioxide != item['dioxido_carbono']:
                        existing_entry.carbon_dioxide = item['dioxido_carbono']
                        updated = True
                    if existing_entry.ethylene != item['etileno']:
                        existing_entry.ethylene = item['etileno']
                        updated = True
                    if existing_entry.ethane != item['etano']:
                        existing_entry.ethane = item['etano']
                        updated = True
                    if existing_entry.acetylene != item['acetileno']:
                        existing_entry.acetylene = item['acetileno']
                        updated = True
                    if existing_entry.co2_co_ratio != item['razao_co2_co']:
                        existing_entry.co2_co_ratio = item['razao_co2_co']
                        updated = True
                    if existing_entry.total_combustible_gases != item['total_gases_combustiveis']:
                        existing_entry.total_combustible_gases = item['total_gases_combustiveis']
                        updated = True
                    if existing_entry.total_gases != item['total_gases']:
                        existing_entry.total_gases = item['total_gases']
                        updated = True
                    if updated:
                        session.commit()
               
            session.close()
            return True
        except Exception as e:
            session.rollback()
            raise e