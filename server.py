import flask_login
from flask_login import current_user, user_unauthorized

from data.portal import Portal
from data.question import Question
from init import *
from functions import *
from forms.testform import *
from data.portal import *
from data.question import *


@app.route("/")
@app.route('/possibilities')
def index():
    portals = None
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        portals = db_sess.query(Portal).filter(Portal.assigned_by == current_user.id).all()
    print(portals)
    return render_template("index.html", title='ПрофТестиум', portals=portals)


@app.route('/rates')
def rates():
    return render_template("tarifs.html", title='Тарифы')


@app.route('/integration')
def implementation():
    return render_template('integration.html', title='Внедрение')


@app.route('/reviews')
def reviews():
    db_sess = db_session.create_session()
    reviews = db_sess.query(Review).all()
    form = FormAddReview()
    return render_template('reviews.html', title='Отзывы', reviews=reviews, db=db_sess, user=User, form=form)


@app.route('/portal/<string:portal>/training')
def training(portal):
    if not access_valid(portal):
        return redirect("/")
    db_sess = db_session.create_session()
    pid = db_sess.query(Portal).filter(Portal.tag == portal).first().id
    tests = db_sess.query(Test).filter(Test.linked_to == pid).all()
    return render_template('training.html', title='Мои тесты', portal=portal, tests=tests)


@app.route('/support')
def support():
    return render_template('support.html', title='Поддержка')

@app.route('/faq')
def faq():
    return render_template('FAQ.html', title='Помощь')

@app.route('/confidential')
def confidential():
    return render_template('confidential.html', title='Политика конфиденциальности')

@app.route('/call')
def call():
    return render_template('call.html', title='Обратный звонок')


@app.route('/portal/<string:portal>')
def portal(portal):
    if not access_valid(portal):
        return redirect("/")
    db_sess = db_session.create_session()
    about = db_sess.query(Portal).filter(Portal.tag == portal).first().about
    return render_template('portal.html', title='Портал', portal=portal, about=about)


@app.route('/portal/<string:portal>/<int:test>/<int:quest>', methods=['GET', 'POST'])
def test(portal, test, quest):
    form = TestForm(meta={'csrf': False})
    db_sess = db_session.create_session()
    # print(access_valid(portal, test, quest))
    if not (access_valid(portal, test, quest)):
        return redirect(f"/portal/{portal}/training")
    print(test)
    qtext = db_sess.query(Question).filter(Question.in_test_id == quest, Question.linked_to == test).first()
    return render_template('tests.html', title='Отзывы', portal=portal,
                               test=test, quest=quest, form=form, qtext=qtext.text)



if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run(port=8080, host="127.0.0.1", debug=True)
