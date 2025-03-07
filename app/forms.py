from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,FileField,SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField("Upload Image",validators=[FileRequired(),FileAllowed(["jpg","png"])])