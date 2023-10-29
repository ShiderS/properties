import sqlalchemy
from flask_login import current_user, login_required, logout_user, login_user
from flask import render_template, redirect
from data import db_session
from forms.new_test_form import NewTestForm

from init import *
from forms.user import *
from forms.loginform import *
from data.user import User


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("x")
        if form.password.data != form.password_again.data:
            print(1)
            return render_template('signup.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.mail == form.mail.data).first():
            print(2)
            return render_template('signup.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            login=form.login.data,
            mail=form.mail.data,
            full_name=form.second_name.data + form.name.data + form.patronymic.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        print(3)
        return redirect('/login')
    print(4)
    return render_template('signup.html', message="Неправильный логин или пароль", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.mail == form.mail.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
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


@app.route('/new_test', methods=['GET', 'POST'])
def new_test():
    form = NewTestForm()
    db_sess = db_session.create_session()
    return render_template('new_test.html', form=form)

