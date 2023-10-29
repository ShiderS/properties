import flask_login


from init import *
from functions import *
from forms.testform import *


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
    db_sess = db_session.create_session()
    reviews = db_sess.query(Review).all()
    form = FormAddReview()
    return render_template('reviews.html', title='Отзывы', reviews=reviews, form=form)

@app.route('/support')
def support():
    return render_template('support.html', title='Поддержка')


@app.route('/portal/<string:portal>/<int:test>/<int:quest>', methods=['GET', 'POST'])
def test(portal, test, quest):
    form = TestForm()
    db_sess = db_session.create_session()
    if(db_sess.query(Portal).filter(Portal.tag == portal).first()):
        if(db_sess.query(Question).filter(Question.in_test_id == quest and Portal.linked_to == test).first()):
            qtext = db_sess.query(Question).filter(Question.in_test_id == quest and Portal.linked_to == test).first()
            return render_template('tests.html', title='Отзывы', portal=portal,
                                   test=test, quest=quest, form=form, qtext=qtext.text)
    return redirect("/")


@app.route('/back', methods=['GET', 'POST'])
def q_back_page():
    adr_req = [i for i in request.referrer.split("/")][-4:]
    adr_req[-1] = str(int(adr_req[-1]) - 1)
    back = "/" + "/".join(adr_req)
    return redirect(location=back)


@app.route('/forward', methods=['GET', 'POST'])
def q_forward_page():
    adr_req = [i for i in request.referrer.split("/")][-4:]
    adr_req[-1] = str(int(adr_req[-1]) + 1)
    forward = "/" + "/".join(adr_req)
    return redirect(location=forward)


if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run(port=8080, host="127.0.0.1", debug=True)
