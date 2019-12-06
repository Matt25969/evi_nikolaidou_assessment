from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.model import Users
from flask_login import LoginManager
from application import app

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class FavsForm(FlaskForm):
    year = IntegerField('Year',
         validators=[
             DataRequired(),
             Length(min=4, max=4)
        ]
     )

    country = SpringField('Country',
         validators=[
             DataRequired(),
             Length(min=4, max=50)
        ]
     )

    performer = SpringField('Performer',
         validators=[
             DataRequired(),
             Length(min=1, max=50)
        ]
     )

    song = SpringField('Song',
         validators=[
             DataRequired(),
             Length(min=1, max=10000)
        ]
     )

     submit = SubmitField('Add to favorites!')
     

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
         validators=[
             DataRequired(),
             Length(min=4, max=30)
         ]
     )

    last_name = StringField('Last Name',
         validators=[
             DataRequired(),
             Length(min=4, max=30)
         ]
    )


    email = StringField( 'Email',
            validators=[
                DataRequired(),
                Email()
            ]
    )

    password= PasswordField('Password',
            validators=[
                DataRequired()
            ]
    )

    passwordcheck= PasswordField('Check Password',
            validators=[
                EqualTo('password')
            ]
    )


    submit = SubmitField('Sign Up')

    def validate_email(self,email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is alreadt in use!')
