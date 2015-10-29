from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, validators
from wtforms.validators import DataRequired

class LoginForm(Form):
    release_num= StringField('release', validators=[DataRequired()])

class QASignOffForm(Form):
	qa_signoff= BooleanField('qa_signoff', [validators.Required()])