from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import Email, Length, DataRequired

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired("You must enter your First Name")])
    lastname = StringField('Last Name', validators=[DataRequired("You must enter your Last Name")])
    phonenumber = StringField('Phone Number', validators=[DataRequired("You must enter your Phone")])
    email = StringField('Email', validators=[DataRequired("Email is required"), Email("Email Entered Invalid")])
    password = PasswordField('Password', validators=[DataRequired("Password is required"), Length(min=8, message="Password must be atleast 8 characters")])
    registerbtn = SubmitField('Register')
    loginbtn = SubmitField('Login')

    def valid_firstname(FlaskForm, firstname):
        if len(firstname.data) < 1:
            raise ValidationError('First Name is required')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Email can not be blank"), Email("Email can not be empty")])
    password = PasswordField('Password', validators=[DataRequired("Password field can not be empty")])
    submitbtn = SubmitField("Login")
    signup = SubmitField("Sign Up")

class PostCommentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired("Title Required")])
    comment = TextAreaField('Your comment') #"Text", render_kw={"rows": 80, "cols": 11}
    submit = SubmitField("Post comment")
