
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class UserForm(FlaskForm):
    name = StringField("Enter your name", validators=[
        DataRequired(), Length(min=2, max=10)])
    email = StringField("Email address", validators=[
        DataRequired(), Email()])

    submit = SubmitField("Submit")
