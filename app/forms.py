from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import FileField, StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only')])

