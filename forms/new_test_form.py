from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class NewTestForm(FlaskForm):
    title = StringField('Название теста', validators=[DataRequired()])
    txt_question = StringField('Вопрос:', validators=[DataRequired()])

    txt_answer = StringField('Правильный ответ:', validators=[DataRequired()])

    submit = SubmitField('Добавить тест')
