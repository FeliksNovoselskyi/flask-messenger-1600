# Импортировать socketio-сервер
from app.settings import socketio_server

# Написать обработчик события message
@socketio_server.on("message")
def handle_message_send(data):
    
    socketio_server.emit("message", data)


# socketio_server.on() - обрабатывает socketio-событие
# socketio_server.emit() - отправляет socketio-событие
