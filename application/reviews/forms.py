from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, validators

class ReviewForm(FlaskForm):
    author = StringField("Author", [validators.Length(min=3)])
    name = StringField("Book name", [validators.Length(min=2)])
    review = TextAreaField("Review")
    star = SelectField("Stars", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

    class Meta:
        csrf = False