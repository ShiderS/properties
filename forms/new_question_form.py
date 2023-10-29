from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewQuestForm(FlaskForm):
    txt_question = StringField('Вопрос:', validators=[DataRequired()])

    txt_answer = StringField('Правильный ответ:', validators=[DataRequired()])

    submit = SubmitField('Добавить вопрос')
