from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, EqualTo

class RegisterForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Password Confirmation',validators=[DataRequired()])