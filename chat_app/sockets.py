import flask
import flask_login
from flask_socketio import join_room, leave_room
from app.settings import socketio_server
from chat_app.models import Message
from .app import online_users
from app.db import DATABASE as DB
from .models import Chat


@socketio_server.on("message")
def handle_message_send(data):
    
    if not flask_login.current_user.is_authenticated:
        return
    
    message = data.get("message")
    chat_id = data.get("chat_id")
    
    new_message = Message(
        user_id=flask_login.current_user.id,
        content=message,
        chat_id=chat_id
    )
    
    DB.session.add(new_message)
    DB.session.commit()
    
    
    socketio_server.emit(
        "message", 
        {"message": message},
        to=f"room_of_group_{chat_id}"
    )


@socketio_server.on("join_group_room")
def handle_join_group_room(data):
    
    join_room(f"room_of_group_{data["chat_id"]}")


@socketio_server.on("user_connect")
def handle_user_connect(data: dict):
    
    
    if flask_login.current_user.id not in online_users.keys():
        online_users[flask_login.current_user.id] = set()
    
    online_users[flask_login.current_user.id].add(flask.request.sid)
    
    
    chat_id = data.get("chat_id", None)
    chat = Chat.query.get(chat_id)
    
    members = []
    
    for user in chat.users:
        
        members.append({
            "is_online": True if user.id in online_users.keys() else False,
            "email": user.email
        })
    
    socketio_server.emit(
        "display_status",
        {
            "online_users": list(online_users.keys()),
            "members": members
        }
    )
