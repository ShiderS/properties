from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField

from wtforms.validators import DataRequired


class FormAddReview(FlaskForm):
    comment = TextAreaField('Комментарий', validators=[DataRequired()])

    submit = SubmitField('Оставить отзыв')