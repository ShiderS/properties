# import flask_login
from flask import Flask, request, render_template, make_response, session, redirect
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask_wtf import FlaskForm
from jinja2 import FileSystemLoader, Environment
from data import db_session


app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = 'secret_key'
# login_manager = LoginManager()
# login_manager.init_app(app)
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run()
    app.run(port=8080, host="127.0.0.1")
