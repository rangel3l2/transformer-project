import gspread as gc
from infrasctructure.database.models import Parameter
from infrasctructure.adapters.Base import Base
class ParameterRepository:
    def __init__(self, connected_sheets=None, sheet_name=None, database_adapter =None):
        self.connected_sheets = connected_sheets
        self.database_adapter = database_adapter
        self.sheet_name = sheet_name
    def work_sheet(self):
        return self.connected_sheets.worksheet(self.sheet_name)
    
    def insert_parameter(self, parameter):
        
        try:
            session = self.database_adapter.get_session()
            Base.metadata.tables['Parametro'].create(self.database_adapter.engine, checkfirst=True)

            for item in parameter:
                existing_entry = session.query(Parameter).filter_by(id_parameter=item['idParametro']).first()
                if not existing_entry:
                    parameter = Parameter(id_parameter=item['idParametro'],num_sample=item['numAmostra'], sampler=item['amostrador'], energized=item['energizado'], oil_type=item['tipoOleo'], temp_sample=item['tempAmostra'], temp_equip=item['tempEquip'], temp_env=item['tempAmbiente'], relative_umidity=item['umidadeRelativa'], sampling_point=item['pontoAmostragem'], reason_analisys=item['motivoAnalise'], dielectric_loss_factors100g=item['fatorPerdasDieletricas100g'], dielectric_loss_factors25g=item['fatorPerdasDieletricas25g'], dielectric_loss_factors90g=item['fatorPerdasDieletricas90g'], dielectric_rigidity=item['rigidezDieletricas'], water_content=item['teorAgua'], indice_neutralization=item['indiceNeutralizacao'], interfacial_tension=item['tensaoInterfacial'], color=item['cor'], param_color=item['paramCor'], visual_aspect=item['aspectoVisual'])
                    session.add(parameter)
                    session.commit()
            session.close()
            return True
        except Exception as e:
            raise e
    
    def get_parameter(self):
        try:
            session = self.database_adapter.get_session()
            parameter = session.query(Parameter).all()
            session.close()
            for item in parameter:
                if hasattr(item, '_sa_instance_state'):
                    item.__dict__.pop('_sa_instance_state')
                
            #transformar equipment em dict
            
            parameter = [item.__dict__ for item in parameter]      
            return parameter
        except Exception as e:
            raise e
    
        
    