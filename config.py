import os


class Config(object):
    """
    Configuration class for the Flask application.

    Attributes:
        SECRET_KEY (str): Secret key for secure session management.
        DEBUG (bool): Debug mode indicator, retrieved from the environment variable.
        SQLALCHEMY_DATABASE_URI (str): URI for the database connection.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Toggle for tracking modifications to database objects.

    Note:
        The database URI is set to use SQLite by default, with the database file named "sqlite.db".

    Example Usage:
        ```
        app.config.from_object(Config)
        ```

    Environment Variables:
        - SECRET_KEY: Secret key for secure session management.
        - DEBUG: Debug mode indicator (True or False).
    """

    SECRET_KEY = os.environ.get("SECRET_KEY", None)
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
