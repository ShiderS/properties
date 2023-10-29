from init import *
from functions import *


@app.route("/")
def index():
    return render_template("index.html", title='ПрофТестиум')


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


if __name__ == "__main__":
    db_session.global_init("db/db.db")
    app.run(port=8080, host="127.0.0.1")
