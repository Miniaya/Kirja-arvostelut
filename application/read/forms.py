from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators
from wtforms_validators import AlphaSpace

class ReadForm(FlaskForm):
    author = StringField("Author", [validators.Length(min=3, max=144), AlphaSpace()])
    name = StringField("Book name", [validators.Length(min=2, max=144)])
    read = BooleanField("I've read this book")

    class Meta:
        csrf = False