from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import Email, Length, InputRequired

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[Length(min=1, message="First Required")])
    lastname = StringField('Last Name', validators=[InputRequired(message = 'You must enter your Last Name')])
    phonenumber = StringField('Phone Number', validators=[InputRequired(message = 'You must enter your Phone')])
    email = StringField('Email', validators=[InputRequired(message = 'Email is required'), Email('Email Entered Invalid')])
    password = PasswordField('Password', validators=[InputRequired(message = "Password is required"), Length(min=8, message="Password must be atleast 8 characters")])
    registerbtn = SubmitField('Register')
    loginbtn = SubmitField('Login')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(message = 'Email can not be blank'), Email('Email can not be empty')])
    password = PasswordField('Password', validators=[InputRequired(message = 'Password field can not be empty')])
    submitbtn = SubmitField("Login")
    signup = SubmitField("Sign Up")

class PostCommentForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired("Title Required")])
    comment = TextAreaField('Your comment') #"Text", render_kw={"rows": 80, "cols": 11}
    submit = SubmitField("Post comment")

class DiaryForm(FlaskForm):
    eventname = StringField('Title', validators=[InputRequired("Title Required")])
    event = TextAreaField('Your comment') #"Text", render_kw={"rows": 80, "cols": 11}
    submit = SubmitField("Add Event")

class API_Resigration(FlaskForm):
    """Registration backed for API Registration"""
    firstname = StringField('First Name', validators=[Length(min=1, message="First Required")])
    lastname = StringField('Last Name', validators=[InputRequired(message = 'You must enter your Last Name')])
    phonenumber = StringField('Phone Number', validators=[InputRequired(message = 'You must enter your Phone')])
    email = StringField('Email', validators=[InputRequired(message = 'Email is required'), Email('Email Entered Invalid')])
    password = PasswordField('Password', validators=[InputRequired(message = "Password is required"), Length(min=6, message="Password must be atleast 6 characters")])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(message = "Confirmation of password is required"), Length(min=6, message="Password must be atleast 6 characters")])
    username = StringField('Enter username', validators=[InputRequired(message = "Username is required")])
    version = StringField('version', validators=[InputRequired(message = "Version is required")])
class Token(FlaskForm):
    """Registration backed for API Registration"""
    username = StringField('Username', validators=[Length(min=1, message="First Required")])
    password = PasswordField('Password', validators=[InputRequired(message = 'You must enter your Last Name')])
