from flask import Flask
from flask_login import LoginManager
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)