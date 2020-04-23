from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ReadForm(FlaskForm):
    author = StringField("Author", [validators.Length(min=3), validators.length(max=144)])
    name = StringField("Book name", [validators.Length(min=2), validators.length(max=144)])
    read = BooleanField("I've read this book")

    class Meta:
        csrf = False