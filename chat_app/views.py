import flask
from chat_app.models import User

from app.db import DATABASE
import werkzeug

# Werkzeug - библиотека для работы с хешами

# DATABASE db.py

def render_chat():
    return flask.render_template("chat.html")

def render_reg():
    # print(flask.request)
    
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        
        # DATABASE - контроль БД
        
        # Пустота полей
        if email and password and confirm_password:
            
            # Совпадение паролей
            if password == confirm_password:
                
                password_hash = werkzeug.security.generate_password_hash(password)
                
                user = User(
                    email = email, 
                    password = password_hash
                )
                
                
                # Добавляем пользователя в отслеживании сессии
                DATABASE.session.add(user)
                
                # Выполняем действие в БД
                DATABASE.session.commit()
    
    return flask.render_template("registration.html")

# хеш невозможно расшифровать 
# все нежные данные в БД - хешируем