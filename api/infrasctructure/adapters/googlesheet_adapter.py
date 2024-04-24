import gspread as gc
class GoogleSheetAdapter:
    def __init__(self, credencial_key_path, id_sheet):
        try:
            self.credecial_key_path = credencial_key_path
            self.id_sheet = id_sheet
        except Exception as e:
            raise e
    def connect_sheets(self):
        gh = gc.service_account(filename=self.credecial_key_path)        
        return gh.open_by_key(self.id_sheet)
        
    
    
    
    