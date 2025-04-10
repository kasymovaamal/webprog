from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    due_date = DateField('Due Date')
    submit = SubmitField('Save Task')