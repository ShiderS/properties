from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash


class RegisterFormPortal(FlaskForm):
    tag = StringField('Тэг', validators=[DataRequired()])
    title = StringField('Название', validators=[DataRequired()])
    inn = PasswordField('ИНН', validators=[DataRequired()])
    about = TextAreaField('О компании', validators=[DataRequired()])

    submit = SubmitField('Зарегистрировать портал')

    def set_inn(self, inn):
        self.inn = generate_password_hash(inn)

    def check_inn(self, inn):
        return check_password_hash(self.inn, inn)
