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
    def update_parameter(self, parameter):
        try:
            session = self.database_adapter.get_session()
            for item in parameter:
                existing_entry = session.query(Parameter).filter_by(id_parameter=item['idParametro']).first()

                if existing_entry:
                    # Verificando se algum campo é diferente
                    if (
                        existing_entry.num_sample != item['numAmostra'] or
                        existing_entry.sampler != item['amostrador'] or
                        existing_entry.energized != item['energizado'] or
                        existing_entry.oil_type != item['tipoOleo'] or
                        existing_entry.temp_sample != item['tempAmostra'] or
                        existing_entry.temp_equip != item['tempEquip'] or
                        existing_entry.temp_env != item['tempAmbiente'] or
                        existing_entry.relative_umidity != item['umidadeRelativa'] or
                        existing_entry.sampling_point != item['pontoAmostragem'] or
                        existing_entry.reason_analisys != item['motivoAnalise'] or
                        existing_entry.dielectric_loss_factors100g != item['fatorPerdasDieletricas100g'] or
                        existing_entry.dielectric_loss_factors25g != item['fatorPerdasDieletricas25g'] or
                        existing_entry.dielectric_loss_factors90g != item['fatorPerdasDieletricas90g'] or
                        existing_entry.dielectric_rigidity != item['rigidezDieletricas'] or
                        existing_entry.water_content != item['teorAgua'] or
                        existing_entry.indice_neutralization != item['indiceNeutralizacao'] or
                        existing_entry.interfacial_tension != item['tensaoInterfacial'] or
                        existing_entry.color != item['cor'] or
                        existing_entry.param_color != item['paramCor'] or
                        existing_entry.visual_aspect != item['aspectoVisual']
                    ):
                        # Atualizando os campos apenas se forem diferentes
                        existing_entry.num_sample = item['numAmostra']
                        existing_entry.sampler = item['amostrador']
                        existing_entry.energized = item['energizado']
                        existing_entry.oil_type = item['tipoOleo']
                        existing_entry.temp_sample = item['tempAmostra']
                        existing_entry.temp_equip = item['tempEquip']
                        existing_entry.temp_env = item['tempAmbiente']
                        existing_entry.relative_umidity = item['umidadeRelativa']
                        existing_entry.sampling_point = item['pontoAmostragem']
                        existing_entry.reason_analisys = item['motivoAnalise']
                        existing_entry.dielectric_loss_factors100g = item['fatorPerdasDieletricas100g']
                        existing_entry.dielectric_loss_factors25g = item['fatorPerdasDieletricas25g']
                        existing_entry.dielectric_loss_factors90g = item['fatorPerdasDieletricas90g']
                        existing_entry.dielectric_rigidity = item['rigidezDieletricas']
                        existing_entry.water_content = item['teorAgua']
                        existing_entry.indice_neutralization = item['indiceNeutralizacao']
                        existing_entry.interfacial_tension = item['tensaoInterfacial']
                        existing_entry.color = item['cor']
                        existing_entry.param_color = item['paramCor']
                        existing_entry.visual_aspect = item['aspectoVisual']
                        session.commit()
            session.close()
            return True
        except Exception as e:
            session.rollback()
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
    
        
    