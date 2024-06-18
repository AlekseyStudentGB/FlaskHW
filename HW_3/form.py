from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class NewUser(FlaskForm):
    name = StringField('User name', validators=[DataRequired(), Length(3)])
    surname = StringField('User surname', validators=[DataRequired(), Length(3)])
    email_user = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6)])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])


