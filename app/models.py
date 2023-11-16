from datetime import datetime
from flask_login import UserMixin
from app.extensions import db, bcrypt


class User(db.Model, UserMixin):
    """
    User class representing a registered user in the application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user (unique and non-nullable).
        password (str): The hashed password of the user.
        messages_sent (Relationship): Relationship to messages sent by the user.
        messages_received (Relationship): Relationship to messages received by the user.

    Methods:
        set_password(password: str): Set the user's password after hashing.
        check_password(password: str): Check if the provided password matches the stored hashed password.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128))
    messages_sent = db.relationship(
        "Message", foreign_keys="Message.sender_id", backref="sender", lazy="dynamic"
    )
    messages_received = db.relationship(
        "Message",
        foreign_keys="Message.recipient_id",
        backref="recipient",
        lazy="dynamic",
    )

    def set_password(self, password):
        """Set the user's password after hashing.

        Args:
            password (str): The plain-text password to be hashed.
        """
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Check if the provided password matches the stored hashed password.

        Args:
            password (str): The plain-text password to be checked.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.username}"


class Message(db.Model):
    """
    Message class representing a message sent between users.

    Attributes:
        id (int): The unique identifier for the message.
        sender_id (int): The user ID of the message sender.
        recipient_id (int): The user ID of the message recipient.
        body (str): The content of the message.
        timestamp (datetime): The timestamp of when the message was sent.

    Methods:
        None
    """

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Message {self.body}>"
