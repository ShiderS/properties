from flask import Flask, request, render_template, make_response, session, redirect
from data import db_session

from init import *
from functions import *

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run()
    app.run(port=8080, host="127.0.0.1")
