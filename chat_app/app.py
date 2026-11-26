import flask


chat_app_blueprint = flask.Blueprint(
    import_name = "chat_app",
    name = "chat",
    static_folder = "static",
    template_folder = "templates",
    static_url_path = "/chat/static/"
)

online_users = {}


"""
online_users =  {
    id_пользователя: {
        sid_клиентов_пользователя,
        sid_клиентов_пользователя
    }
}
"""
