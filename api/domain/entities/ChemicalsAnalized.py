from infrasctructure.database.models import ChemicalAnalized

class ChemicalsAnalized(ChemicalAnalized):
     def __init__(self, hydrogen, oxygen, nitrogen, carbon_monoxide, methane, carbon_dioxide, ethylene, ethane, acetylene, co2_co_ratio, total_combustible_gases, total_gases, id_chemical_analized=None):
        self.id_chemical_analized = id_chemical_analized
        self.hydrogen = hydrogen
        self.oxygen = oxygen
        self.nitrogen = nitrogen
        self.carbon_monoxide = carbon_monoxide
        self.methane = methane
        self.carbon_dioxide = carbon_dioxide
        self.ethylene = ethylene
        self.ethane = ethane
        self.acetylene = acetylene
        self.co2_co_ratio = co2_co_ratio
        self.total_combustible_gases = total_combustible_gases
        self.total_gases = total_gases