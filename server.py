from flask import Flask, request, render_template, make_response, session, redirect
from data import db_session
from data.user import User

from forms.loginform import LoginForm
from forms.user import RegisterForm


from init import *
from functions import *


@app.route("/")
def index():
    return render_template("index.html", title='ПрофТестиум')


@app.route('/possibilities')
def possibilities():
    return render_template('possibilities.html', title='Возможности')


@app.route('/rates')
def rates():
    return render_template('rates.html', title='Тарифы')


@app.route('/implementation')
def implementation():
    return render_template('implementation.html', title='Внедрение')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title='Отзывы')




if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run(port=8080, host="127.0.0.1")
