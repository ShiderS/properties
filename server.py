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
    db_sess = db_session.create_session()
    reviews = db_sess.query(Review).all()
    return render_template('reviews.html', title='Отзывы')


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
