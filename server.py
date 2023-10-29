from flask import Flask, request, render_template, make_response, session, redirect, url_for
from data import db_session
from data.user import User

from forms.loginform import LoginForm
from forms.testform import TestForm
from forms.user import RegisterForm

from init import *
from functions import *


@app.route("/")
@app.route('/possibilities')
def index():
    return render_template("index.html", title='ПрофТестиум')

@app.route('/rates')
def rates():
    return render_template("tarifs.html", title='Тарифы')


@app.route('/integration')
def implementation():
    return render_template('integration.html', title='Внедрение')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title='Отзывы')

@app.route('/support')
def support():
    return render_template('support.html', title='Поддержка')


@app.route('/portal/<string:portal>/<int:test>/<int:quest>', methods=['GET'])
def test(portal, test, quest):
    form = TestForm
    db_sess = db_session.create_session()

    return render_template('tests.html', title='Отзывы', portal=portal, test=test, quest=quest, form=form)


@app.route('/back', methods=['GET', 'POST'])
def q_back_page():
    adr_req = [i for i in request.referrer.split("/")][-4:]
    adr_req[-1] = str(int(adr_req[-1]) - 1)
    back = "/" + "/".join(adr_req)
    # print(back)
    # print(request.method)
    # redirect(location=back)
    return redirect(location=back)


@app.route('/forward', methods=['GET', 'POST'])
def q_forward_page():
    adr_req = [i for i in request.referrer.split("/")][-4:]
    adr_req[-1] = str(int(adr_req[-1]) + 1)
    forward = "/" + "/".join(adr_req)
    # print(forward)
    # print(request.method)
    return redirect(location=forward)


if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run(port=8080, host="127.0.0.1", debug=True)
