from flask import Blueprint, render_template
from flask_login import login_required

chat = Blueprint("chat", __name__)


@chat.route("/")
@login_required
def chat_users():
    return render_template("chat/global_chat.html", title="Chats")
