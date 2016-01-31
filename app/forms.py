from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddListingForm(Form):
    description = StringField('description', Validators=[DataRequired()])
    location = StringField('openid', validators=[DataRequired()])
    section = StringField('openid', validators=[DataRequired()])
    start_time = StringField('openid', validators=[DataRequired()])
    stop_time = StringField('openid', validators=[DataRequired()])
    subject = StringField('openid', validators=[DataRequired()])
    title = StringField('openid', validators=[DataRequired()])
