class ChangeDetector:
    def __init__(self, spreadsheet_id, callback):
        self.spreadsheet_id = spreadsheet_id
        self.callback = callback

    def start_monitoring(self, sheet_name):
        sheet = self.sheet_client.open_spreadsheet(self.spreadsheet_id).sheet1
        watch_id = sheet.watch_delta_range(
        'A1:B', callback=self.on_change_detected
        )
        print(f"Monitoramento iniciado na planilha '{sheet_name}' (watch_id: {watch_id})")
        

    def stop_monitoring(self):        
        pass
  
