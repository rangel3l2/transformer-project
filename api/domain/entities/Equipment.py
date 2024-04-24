from infrasctructure.database.models import Equipment
class Equipment(Equipment):
    def __init__(self, serie_id, owner, tag, place_installed, manufacturer, year_of_manufacture, tension_primary, tension_secondary, volume_of_oil, sampling_address, max_power  ):
        self.serie_id = serie_id
        self.owner = owner
        self.tag = tag 
        self.place_installed = place_installed
        self.manufacturer = manufacturer
        self.year_of_manufacture = year_of_manufacture
        self.tension_primary = tension_primary
        self.tension_secondary = tension_secondary
        self.max_power = max_power
        self.volume_of_oil = volume_of_oil
        self.sampling_address = sampling_address
        
    def __dict__(self):
        return {'serie_id': self.serie_id, 'owner': self.owner, 'tag': self.tag, 'place_installed': self.place_installed, 'manufacturer': self.manufacturer, 'year_of_manufacture': self.year_of_manufacture, 'tension_primary': self.tension_primary, 'tension_secondary': self.tension_secondary, 'max_power': self.max_power, 'volume_of_oil': self.volume_of_oil, 'sampling_address': self.sampling_address}