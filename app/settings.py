import flask
import os
import flask_socketio

main_app = flask.Flask(
    import_name = "app",
    instance_path = os.path.abspath(os.path.join(__file__,"..", "instance"))
)

socketio_server = flask_socketio.SocketIO(main_app)