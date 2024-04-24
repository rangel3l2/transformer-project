from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum as EnumSQL, Float
from infrasctructure.adapters.Base import Base
from sqlalchemy.orm import relationship
import uuid

uuid_str = str(uuid.uuid4())
class Analisys(Base):
    __tablename__ = 'Analise'
    id_analisys = Column(Integer, primary_key=True, unique=True, nullable=False,
                         name='id_analise')
    enter_date = Column(DateTime, nullable=False, name='data_entrada')
    sampling_date = Column(DateTime, name='data_amostragem')
    status = Column(String(45), nullable=False)
    serie_id = Column(Integer, ForeignKey('Equipamento.serieid'), name='serieid')
    id_parameter = Column(Integer, ForeignKey('Parametro.id_parametro'), name='id_parametro')    
    
class Parameter(Base):
    __tablename__ = 'Parametro'
    id_parameter = Column(Integer, primary_key=True, unique=True, nullable=False,
                          name='id_parametro')
    num_sample = Column(Integer, nullable=False, name='num_amostra')
    sampler = Column(String(45), name='amostrador') 
    energized = Column(String(45), name='energizado')  
    oil_type = Column(String(45), nullable=False, name='tipooleo')
    temp_sample = Column(Float, nullable=False, name='tempamostra')
    temp_equip = Column(Float, nullable=False, name='tempequip')
    temp_env = Column(Float, nullable=False, name='tempambiente')
    relative_umidity = Column(Float, nullable=False, name='umidaderelativa')
    sampling_point = Column(String(45), nullable=False, name='pontoamostragem')
    reason_analisys = Column(String(45), nullable=False, name='motivoanalise')
    dielectric_loss_factors100g = Column(Float, name='fatorperdasdieletricas100g')
    dielectric_loss_factors25g = Column(Float, nullable=False, name= 'fatorperdasdieletricas25g')
    dielectric_loss_factors90g = Column(Float, nullable=False, name='fatorperdasdieletricas90g')
    dielectric_rigidity = Column(Float, nullable=False, name= 'rigidezdieletricas')
    water_content = Column(Float, nullable=False, name ='teoragua')
    indice_neutralization = Column(Float, nullable=False, name= 'indiceneutralizacao')
    interfacial_tension = Column(Float, nullable=False, name='tensaointerfacial')
    color = Column(String(45), name='cor')  
    param_color = Column(String(45), name='paramcor')  
    visual_aspect = Column(String(45), name = 'aspectovisual') 

class Equipment(Base):
    __tablename__ = 'Equipamento'  
    serie_id = Column(Integer, nullable=False, name='serieid', primary_key=True, unique=True)
    owner = Column(String(45), nullable=False, name='proprietario')
    tag = Column(String(45), nullable=False, name='tag')
    place_installed = Column(String(45), nullable=False, name='localinstalacao')
    manufacturer = Column(String(45), nullable=False, name='fabricante')
    year_of_manufacture = Column(Integer, nullable=False, name='anofabricacao')
    tension_primary = Column(Float, nullable=False, name='tensaoprimaria')
    tension_secondary = Column(Float, nullable=False, name='tensaosecundaria')
    max_power = Column(Float, nullable=False, name='maxPotencia')
    volume_of_oil = Column(Float, nullable=False, name='volumeoleo')
    sampling_address = Column(String(45), name='enderecoamostragem')