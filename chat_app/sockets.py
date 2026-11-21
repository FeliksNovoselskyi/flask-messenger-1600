import flask_login
from flask_socketio import join_room, leave_room
from app.settings import socketio_server
from chat_app.models import Message
from app.db import DATABASE as DB


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
