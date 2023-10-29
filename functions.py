import sqlalchemy
from flask_login import current_user, login_required, logout_user, login_user
from flask import render_template, redirect, request, url_for
from data import db_session
from data.mail_check import send_mail, mail_codes
from forms.new_test_form import NewTestForm
from forms.verifform import VerifForm

from init import *
from forms.user import *
from forms.loginform import *
from forms.add_review import *
from data.user import User
from data.review import *


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={'csrf':False})
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
        full_name = form.second_name.data + form.name.data + form.patronymic.data
        user_data = f'{form.login.data}+{form.mail.data}+{full_name}+{form.password.data}'
        send_mail("proftestium56@gmail.com", "lhnu gcsw jpyr tmhc", form.mail.data)
        return redirect(url_for("mail_verification", data=user_data))
        #return redirect('/mail_verification')
    return render_template('signup.html', message="Неправильный логин или пароль", form=form)


@app.route('/mail_verification<data>', methods=['GET', 'POST'])
def mail_verification(data):
    form = VerifForm(meta={'csrf':False})
    if form.validate_on_submit():
        data = data.split('+')
        if form.code.data == str(mail_codes[data[1]]):
            db_sess = db_session.create_session()
            user = User(
                login=data[0],
                mail=data[1],
                full_name=data[2]
            )
            user.set_password(data[3])
            db_sess.add(user)
            db_sess.commit()
            return redirect('/login')
        return render_template('mail_verification.html', title='Подтверждение почты',
                               form=form,
                               message="Неверный код")
    return render_template('mail_verification.html', message="Неправильный код", form=form)





@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf':False})
    if form.validate_on_submit():
        print(1)
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.mail == form.mail.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('index.html',
                               message="Неправильный логин или пароль",
                               form=form)
    print(2)
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


@app.route('/add_review', methods=['GET', 'POST'])
@login_required
def add_review():
    form = FormAddReview
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        id = current_user.get_id()
        if form.validate_on_submit():
            title = request.form.get('text')
            review = Review(
                id_user=id,
                title=title
            )
            db_sess.add(review)
            db_sess.commit()
