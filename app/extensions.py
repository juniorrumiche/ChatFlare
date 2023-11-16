from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
socketio = SocketIO()
login_manager = LoginManager()

"""
Flask extensions for various functionalities in the application.

- `db` (SQLAlchemy): SQLAlchemy extension for database interaction.
- `bcrypt` (Bcrypt): Bcrypt extension for password hashing.
- `socketio` (SocketIO): SocketIO extension for real-time communication.
- `login_manager` (LoginManager): LoginManager extension for user authentication.

These extensions are initialized with the Flask application instance in the application factory.
"""
