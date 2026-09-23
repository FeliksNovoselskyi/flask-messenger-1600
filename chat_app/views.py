
import flask
import werkzeug.security
from chat_app.models import User
import flask_login

from app.db import DATABASE
import werkzeug
from chat_app.models import User


def render_chat():
    
    if flask_login.current_user.is_authenticated:
        data = {
            "can_logout": True
        }
        
        return flask.render_template("chat.html", **data)
    
    return flask.render_template("chat.html")

def render_reg():
    
    if flask_login.current_user.is_authenticated: 
        return flask.redirect("/")
        

    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        
        if email and password and confirm_password:
            
            if password == confirm_password:
                
                password_hash = werkzeug.security.generate_password_hash(password)
                
                user = User(
                    email = email, 
                    password = password_hash
                )
                
                DATABASE.session.add(user)
                DATABASE.session.commit()
                
                return flask.redirect("/auth")
            # Полина
            else:
                data = {
                    "error": "Пароли не совпадают",
                    "email": email,
                    "password": password,
                    "confirm_password": confirm_password
                }
                return flask.render_template("registration.html", **data)
            
        # Женя
        else:
            data = {
                "error": "Заполните все поля",
                "email": email,
                "password": password,
                "confirm_password": confirm_password
            }
            return flask.render_template("registration.html", **data)
    
    return flask.render_template("registration.html")


def render_auth():
    
    # flask_login.current_user - объект текущего пользователя
    # flask_login.current_user.is_authenticated - запись о том, есть ли сессия у пользователя
    # is_authenticated - True/False
    
    if flask_login.current_user.is_authenticated:
        return flask.redirect("/")
    
    # flask.redirect() - меняет страницу пользователя
    
    # Полина: проверяем тип запроса, получаем почту и пароль
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        
        if email and password:
            # Полина: проверяем совпадает ли почта
            user = User.query.filter_by(email = email)
            
            # Он отправляет запрос, возвращает объект пользователя
            user = user.scalar()
            
            if user:
                # Полина: проверяем правильность пароля и хешируем его
                is_correct_password = werkzeug.security.check_password_hash(
                    pwhash=user.password, 
                    password = password
                )
                
                
                if is_correct_password:
                    # Богдан: проверка пользователя
                    flask_login.login_user(user=user)
                    
                    return flask.redirect('/')
                
                else:
                    # Богдан: проверка логина и пароля
                    data = {
                        "error": "Логин или пароль неверны",
                        "email": email,
                        "password": password
                    }
                    # Богдан: **data - распаковка словаря
                    return flask.render_template("auth.html", **data)
                
            else:
                data = {
                    "error": "Такого пользователя нету",
                    "email": email,
                    "password": password
                }
                return flask.render_template("auth.html", **data)
        else:
            data = {
                "error": "Заполните все поля",
                "email": email,
                "password": password
            }
            return flask.render_template("auth.html", **data)
        
    return flask.render_template("auth.html")


# redirect - обязательный return
# render_template - обязательный return

def render_logout():
    
    # Егор Войтов: выходит из аккаунта
    flask_login.logout_user()
    
    # Егор Войтов: перенаправляет на страницу авторизации
    return flask.redirect("/auth")
