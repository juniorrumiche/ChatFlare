from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    """
    Form class for user login.

    Attributes:
        username (StringField): Field for entering the username.
        password (PasswordField): Field for entering the password.
        submit (SubmitField): Button for submitting the login form.

    Validators:
        - username: Required, length between 4 and 30 characters.
        - password: Required, length between 5 and 30 characters.
    """

    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(4, 30, message="Username must be between 4 and 30 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(5, 30, message="Password must be between 5 and 30 characters."),
        ],
    )
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    """
    Form class for user registration.

    Attributes:
        username (StringField): Field for entering the username.
        password (PasswordField): Field for entering the password.
        password_confirm (PasswordField): Field for confirming the password.
        submit (SubmitField): Button for submitting the registration form.

    Validators:
        - username: Required, length between 4 and 30 characters.
        - password: Required, length between 5 and 30 characters.
        - password_confirm: Required, must be equal to the password.
    """

    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(4, 30, message="Username must be between 4 and 30 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(5, 30, message="Password must be between 5 and 30 characters."),
        ],
    )
    password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Confirmation of password is required."),
            EqualTo("password", message="Passwords do not match."),
        ],
    )
    submit = SubmitField("Sign Up")
