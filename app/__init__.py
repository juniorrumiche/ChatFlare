from flask import Flask

from config import Config
from app.auth.routes import auth
from app.extensions import db, socketio, bcrypt, login_manager
from app.chat.events import *  # noqa
from app.models import User
from app.chat.routes import chat


def create_app(config_class=Config):
    """
    Application factory function for creating a Flask application.

    Args:
        config_class (Config): The configuration class for the application.

    Returns:
        Flask: The Flask application instance.
    """
    # Create the application instance
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the application
    db.init_app(app)
    socketio.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Register blueprints for different parts of the application
    app.register_blueprint(auth, url_prefix="/auth", name="auth")
    app.register_blueprint(chat, url_prefix="/", name="chat")

    @login_manager.user_loader
    def load_user(user_id):
        """
        Callback function to load a user by their ID.

        Args:
            user_id (int): The ID of the user to load.

        Returns:
            User: The user corresponding to the provided ID.
        """
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    return app
