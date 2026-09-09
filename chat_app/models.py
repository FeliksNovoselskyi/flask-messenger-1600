
from app.db import DATABASE as DB


class User(DB.Model):
    
    # Тип поля указываем первым
    id = DB.Column(DB.Integer, primary_key = True)
    email = DB.Column(DB.String)
    
    # password
    password = DB.Column(DB.String)


# модель - шаблон таблицы
# таблица - часть БД, в которой хранятся


# модель - шаблон записи