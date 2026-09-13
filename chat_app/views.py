import flask
from chat_app.models import User
import flask_login

from app.db import DATABASE
import werkzeug



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

# Паша
# Создать функцію отображенія шаблона auth.html

def render_auth():
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        
        if email and password:
            user = User.query.filter_by(email = email)
            
            # SELECT user.id AS user_id, user.email AS user_email, user.password AS user_password 
            # FROM user 
            # WHERE user.email = ?
            print("\n", user)
            
            
            if user:
                # Он отправляет запрос, возвращает объект пользователя
                user = user.scalar()
                
                # <User 1> felixdnbox@gmail.com
                print(user, user.email)

                flask_login.login_user(user=user)
            
            
    return flask.render_template("auth.html")
