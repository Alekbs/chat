from models import *
import socket
import json


def ck_login(login, passw):
    print(f"{type(login)} : {login}, {type(passw)} : {passw}")
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
            users = User(
                login=login, password=passw, phone=phone, avatar="1"
            ).save()  # Создаем новую запись пользователя
    except IntegrityError:
        # Если пользователь с таким логином уже существует (уникальность нарушена)
        return "Пользователь с таким логином уже существует."
    return "Регистрация успешно завершена."


print(ck_login("admin", "1234"))
# Создаем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Определяем хост и порт, на котором сервер будет слушать
host = input("Введите ip: ")
port = 8000

# Привязываем сокет к хосту и порту
server_socket.bind((host, port))

# Начинаем прослушивать соединения
server_socket.listen(1)

print(f"Сервер слушает на {host}:{port}")

while True:
    # Принимаем входящее соединение
    client_socket, client_address = server_socket.accept()
    print(f"Получено соединение с {client_address}")

    # Принимаем данные от клиента
    data = client_socket.recv(1024)

    if not data:
        break

    # Декодируем JSON-данные от клиента
    request_data = json.loads(data.decode("utf-8"))

    # Определяем, какую функцию вызывать
    function_name = request_data.get("function")

    if function_name == "ck_login":
        # Выполняем функцию ck_login с переданными аргументами
        username = request_data.get("username")
        password = request_data.get("password")
        result = ck_login(username, password)
    elif function_name == "register":
        # Выполняем функцию ck_login с переданными аргументами
        username = request_data.get("username")
        password = request_data.get("password")
        phone = request_data.get("phone")
        result = register(username, password, phone)
    else:
        result = "Неизвестная функция"

    # Отправляем результат обратно клиенту
    response_data = json.dumps({"result": result}).encode("utf-8")
    client_socket.send(response_data)

    # Закрываем соединение с клиентом
    client_socket.close()

# Закрываем серверный сокет
server_socket.close()
