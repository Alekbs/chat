from handler.models import *


def ck_login(login, passw):
    try:
        user = User.get(User.login == login)  # Ищем пользователя по логину
        if user.password == passw:  # Сравниваем пароль
            return True  # Вернуть True, если пароль совпадает
    except User.DoesNotExist:
        pass  # Если пользователь не найден, просто пропустить

    return False  # Вернуть False, если логин или пароль не совпадают



def register(login, passw, phone):
    try:
        print(login, passw, phone)
        # Начинаем транзакцию для безопасной вставки
        with db:
            users = User(login=login, password=passw, phone=phone, avatar='1').save() # Создаем новую запись пользователя
    except IntegrityError:
        # Если пользователь с таким логином уже существует (уникальность нарушена)
        return "Пользователь с таким логином уже существует."
    return "Регистрация успешно завершена."
