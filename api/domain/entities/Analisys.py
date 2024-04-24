from domain.enums import Status
from infrasctructure.database.models import Analisys
class Analisys(Analisys):
    def __init__(self, id_analisys, enter_date, sampling_date, status):
        self.id_analisys = id_analisys
        self.enter_date = enter_date
        self.sampling_date = sampling_date
        self.status = Status(status)
        
    def __dict__(self):
        return {'id_analisys': self.id_analisys, 'enter_date': self.enter_date, 'sampling_date': self.sampling_date, 'status': self.status}