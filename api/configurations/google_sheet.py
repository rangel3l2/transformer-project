from dotenv import load_dotenv, get_key

load_dotenv(".env")

sheets_id = get_key('.env', 'GOOGLESHEETS_ID')
def get_sheets_id():
    return sheets_id
