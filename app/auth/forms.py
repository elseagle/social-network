from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from wtforms import ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                          0,
                                                          'Usernames must have only '
                                                          'letters, numbers, dots or '
                                                          'underscores')
                                                   ]
                           )
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exist')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    new_password = PasswordField('New Password',
                                 validators=[DataRequired(),
                                             EqualTo('new_password2',
                                                     message='New password must match')])
    new_password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Update password')


class ChangeEmailForm(FlaskForm):
    new_email = StringField('New email', validators=[DataRequired(), Email(), Length(1, 64)])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Update password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Enter your email', validators=[DataRequired(), Email(), Length(1, 64)])
    submit = SubmitField('Submit')


class PasswordResetForm(FlaskForm):
    new_password = PasswordField('New Password',
                                 validators=[DataRequired(),
                                             EqualTo('new_password2',
                                                     message='New password must match')])
    new_password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset password')
