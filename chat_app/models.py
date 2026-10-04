import flask_login
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
        # Указивает, мы связываемся с одним объектом, или со множество
        # False - c одним объектом
        # True - с множество
        uselist = False
    )

# Артем: создать модель Chat
class Chat(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    title = DB.Column(DB.String)
    
    user_id = DB.Column(
        DB.Integer, 
        DB.ForeignKey("user.id"),
        unique = True
    )
    
    # DB.ForeignKey("user.id")
    # ForeignKey - заграничный ключ, через него указываем id связаной записи
    # user.id:
        # user - таблица пользователя
        # user.id - столбец с его id
    
    user = DB.relationship(
        "User",
        back_populates="chat"
    )

# Ростик: создать модель Message

class Message(DB.Model):
    
    id = DB.Column(DB.Integer, primary_key = True)
    text = DB.Column(DB.String)