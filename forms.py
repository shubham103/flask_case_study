from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Customer Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Customer SSM Id',
                        validators=[DataRequired(), Email()])
    age = IntegerField('Age',
                           validators=[DataRequired(), Length(min=1, max=2)])
    address = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State',
                           validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')
    #reset = ResetField('Reset')


class LoginForm(FlaskForm):
    userId= StringField('UserId',pvalidators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
