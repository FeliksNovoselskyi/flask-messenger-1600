import flask_login

from .settings import main_app
from chat_app.models import User


# F12 -> Application -> Cookies

main_app.secret_key = "megaprogrammer_228_67"

# Обязательно указываем секретный ключ
# main_app.secret_key - настройка сервера, 
# в которой указываем секретный ключ

login_manager = flask_login.LoginManager(
    app = main_app
)

# login_manager - управленец сессией

# login_manager.user_loader - это стандартная функция 
# загрузки пользователя в flask_login


@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(user_id)

# User.query.get() - получает пользователя по его id