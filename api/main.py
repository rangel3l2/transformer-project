from flask import Flask
from flask_cors import CORS
from presentation import routes
from configurations import db, google_sheet 



db_host = db.get_db_host()
db_port = db.get_db_port()
db_user = db.get_db_user()
db_password = db.get_db_password()
db_name = db.get_db_name()
db_secret_key_jwt = db.get_db_secret_key_jwt()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db.db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#googlesheet
app.config['SHEET_ID'] = google_sheet.get_sheets_id()

app.config['CREDENTIALS_GOOGLE_SHEET'] = 'credentials.json'
app.register_blueprint(routes.api_blueprint)

if __name__ == "__main__":
  
  app.run(debug=True, host='0.0.0.0', port=5000 )
