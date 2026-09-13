from .settings import main_app
from chat_app.views import render_reg
# Импортировать функции отображения
from chat_app.views import render_chat
from chat_app.views import render_auth
from chat_app.app import chat_app_blueprint


main_app.add_url_rule(
    rule = "/",
    view_func = render_chat

)

main_app.add_url_rule(
    rule = "/reg",
    view_func = render_reg,
    methods = ["GET", "POST"]
)

# Егор Столяров
# Указать адрес страніци авторізаціі
main_app.add_url_rule(
    rule = "/auth",
    view_func = render_auth,
    methods = ["GET", "POST"]
)

main_app.register_blueprint(blueprint = chat_app_blueprint)
