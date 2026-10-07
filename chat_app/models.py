import flask_login
from sqlalchemy import Constraint
from app.db import DATABASE as DB

# uq_user_email
# uq - unique - названіе ограніченія
# user - табліца
# email - поле

class User(DB.Model, flask_login.UserMixin):
    
    # Тип поля указываем первым
    id = DB.Column(DB.Integer, primary_key = True)
    email = DB.Column(DB.String, unique = True)
    
    # password
    password = DB.Column(DB.String)

    first_name = DB.Column(DB.String)
    last_name = DB.Column(DB.String)
    username = DB.Column(DB.String)
    gender = DB.Column(DB.Boolean)
    birth_date = DB.Column(DB.DateTime)
    avatar_path = DB.Column(DB.String)
    
    chat = DB.relationship(
        "Chat",
        back_populates = "user",
        uselist = False
    )
    
    # Кирилл
    # One-to-Many
    messages = DB.relationship(
        "Message",
        back_populates = "user",
        uselist = True
    )
    
    # Со сколькими объектами будет связи
    # uselist=True - множество объектов
    # uselist=False - один объект


class Chat(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    title = DB.Column(DB.String)
    
    # user_id
    user_id = DB.Column(
        DB.Integer, 
        DB.ForeignKey("user.id", name="fk_chat_user_id")
    )
    
    # Кирилл
    user = DB.relationship(
        "User",
        back_populates = "chat"
    )


class Message(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    content = DB.Column(DB.String)
    
    user_id = DB.Column(
        DB.Integer, 
        DB.ForeignKey("user.id", name="fk_message_user_id")
    )
    
    # Егор
    # Настроить связь с моделью User
    user = DB.relationship(
        "User",
        back_populates = "messages"
    )

