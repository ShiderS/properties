from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewTestForm(FlaskForm):
    title = StringField('Название теста', validators=[DataRequired()])

    submit = SubmitField('Добавить тест')
