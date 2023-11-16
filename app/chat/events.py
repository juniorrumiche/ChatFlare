from flask_socketio import send, emit, join_room
from flask_login import current_user
from app.extensions import socketio

global_room = "global_room"
online_users = set()


@socketio.on("connect")
def on_connect():
    """
    Event handler for a user connecting to the socket.

    If the user is authenticated, adds the user to the online users set,
    joins the global room, and broadcasts a connection message to the room.

    Returns:
        None
    """
    if current_user.is_authenticated:
        username = current_user.username
        online_users.add(username)
        join_room(global_room)
        send(
            {
                "message": f"{username} has joined the room.",
                "username": username,
                "type": "connect",
            },
            room=global_room,
            broadcast=True,
        )


@socketio.on("disconnect")
def on_disconnect():
    """
    Event handler for a user disconnecting from the socket.

    If the user is authenticated, removes the user from the online users set.

    Returns:
        None
    """
    if current_user.is_authenticated:
        online_users.remove(current_user.username)


@socketio.on("get_online_users")
def send_online_users():
    """
    Event handler for sending online users to the client.

    If the user is authenticated, emits the "online_users" event with a list
    of other online users to the client.

    Returns:
        None
    """
    if current_user.is_authenticated:
        other_users = [user for user in online_users if user != current_user.username]
        emit("online_users", other_users[:10])


@socketio.on("chat_message")
def handle_chat_message(payload):
    """
    Event handler for handling incoming chat messages.

    If the user is authenticated, sends the chat message to the global room.

    Args:
        payload (dict): The payload containing the chat message.

    Returns:
        None
    """
    if not current_user.is_authenticated:
        return False
    username = current_user.username
    message = payload["message"]
    if not message:
        return False
    send(
        {"message": message, "username": username, "type": "message"},
        room=global_room,
    )
