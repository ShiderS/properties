from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class VerifForm(FlaskForm):
    code = StringField('Код', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')