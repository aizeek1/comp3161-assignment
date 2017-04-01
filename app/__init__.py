from flask import Flask
from flask_login import LoginManager
import MySQLdb

app = Flask(__name__)

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

EMPLOYEEID = 'admin'
PASSWORD = 'password123'

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

#connect to database created
db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'HospitalDB')

app.config.from_object(__name__)
from app import views
