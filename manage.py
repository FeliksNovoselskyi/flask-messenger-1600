from app.settings import socketio_server, main_app
from app.loadenv import migration


def main():
    try:
        
        migration()
        
        socketio_server.run(
            app = main_app,
            debug = True,
            port = 8000
        )
        
    except Exception as error:
        print(f"Помилка під час запуску проєкта: {error}")

if __name__ == "__main__":
    main()
