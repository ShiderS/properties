from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired


class FormAddReview(FlaskForm):
    comment = StringField('Комментарий', validators=[DataRequired()])

    submit = SubmitField('Оставить отзыв')