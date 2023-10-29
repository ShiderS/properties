import flask_login
import sqlalchemy
from flask_login import current_user, login_required, logout_user, login_user
from flask import render_template, redirect, request
from data import db_session
from data.portal import Portal
from data.question import Question
from data.test import Test
from forms.new_question_form import NewQuestForm
from forms.new_test_form import NewTestForm

from init import *
from forms.user import *
from forms.loginform import *
from forms.add_review import *
from data.user import User
from data.review import *


def access_valid(portal, test=None, quest=None):
    db_sess = db_session.create_session()
    if (db_sess.query(Portal).filter(Portal.tag == portal).first() and True):
        #print(1)
        if (not test):
            return True
        elif (db_sess.query(Test).filter(Test.id == test).first()):
            #print(2)
            if (not quest):
                return True
            elif (db_sess.query(Question).filter(Question.in_test_id == quest).first()):
                #print(3)
                return True
    return False


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={'csrf': False})
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('signup.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.mail == form.mail.data).first():
            return render_template('signup.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        full_name = form.second_name.data + " " + form.name.data + " " + form.patronymic.data
        user = User(
            login=form.login.data,
            mail=form.mail.data,
            full_name=full_name
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('signup.html', message="Неправильный логин или пароль", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf':False})
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.mail == form.mail.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('index.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/portal/<string:portal>/new_test', methods=['GET', 'POST'])
@login_required
def new_test(portal):
    form = NewTestForm(meta={'csrf': False})
    db_sess = db_session.create_session()
    if (access_valid(portal)):
        if(form.validate_on_submit()):
            test = Test(
                titles=form.title.data,
                linked_to=db_sess.query(Portal).filter(Portal.tag == portal).first().id
            )
            db_sess.add(test)
            db_sess.commit()
            adr_req = [i for i in request.base_url.split("/")][-4:]
            return redirect(f"/portal/{adr_req[-2]}/{test.id}/new_question/1")

    return render_template('new_test.html', title="Новый тест",
                               portal=portal, form=form)


@app.route('/portal/<string:portal>/<int:tid>/new_question/<int:qid>', methods=['GET', 'POST'])
@login_required
def new_question(portal, tid, qid):
    form = NewQuestForm(meta={'csrf': False})
    db_sess = db_session.create_session()
    if (access_valid(portal)):
        if(form.validate_on_submit()):
            quest = Question(
                in_test_id=qid,
                linked_to=tid,
                text=form.txt_question.data,
                answer=form.txt_answer.data,
                qtype=0
            )
            print(form.txt_question.data)
            db_sess.add(quest)
            db_sess.commit()
            adr_req = [i for i in request.base_url.split("/")][-4:]

            return redirect(f"/portal/{adr_req[-4]}/{tid}/new_question/{qid+1}")
    return render_template('new_question.html', title="Новый тест",
                           portal=portal, tid=tid, qid=qid, form=form)
@app.route('/add_review', methods=['GET', 'POST'])
@login_required
def add_review():
    form = FormAddReview(meta={'csrf':False})
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        id = current_user.get_id()
        if form.validate_on_submit():
            title = form.comment.data
            if title != "":
                review = Review(
                    id_user=id,
                    title=title
                )
                db_sess.add(review)
                db_sess.commit()
                return redirect('/reviews')
    return render_template('add_review.html', form=form)
