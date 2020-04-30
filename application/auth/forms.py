from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class SignInForm(FlaskForm):
    name = StringField("Full name", [validators.length(min=2, max=100)])
    username = StringField("Username", [validators.length(min=1, max=24)])
    password = PasswordField("Password", [validators.length(min=3, max=16)])

    class Meta:
        csrf = False