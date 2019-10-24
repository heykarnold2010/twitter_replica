from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class TitleForm(FlaskForm):
    title = StringField('Enter a new header:', validators=[DataRequired()])
    submit = SubmitField('ChangeTitle')


class ContactForm(FlaskForm):
    name = StringField('Name',
    validators=[DataRequired()])
    email = StringField('E-mail',
    validators=[DataRequired(), Email()])
    message = TextAreaField('Message',
    validators=[DataRequired()])
    # show_messages = BooleanField('Show All Data')
    submit = SubmitField('Send Message')

class ShowContactsForm(FlaskForm):
    show_messages = BooleanField('Display Data')
    submit = SubmitField('Show All Data')

class PostForm(FlaskForm):
    tweet = StringField('What are you doing?', validators=[DataRequired(), Length(max=10)])
    submit = SubmitField('Tweet')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name  = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    bio = StringField('Bio')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
