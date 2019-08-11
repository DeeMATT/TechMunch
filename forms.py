from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Email()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    vallidators=[InputRequired(), EqualTo('Confirm')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[InputRequired(), EqualTo('Confirm', message='Passwords must match')])

