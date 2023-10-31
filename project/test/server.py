from flet.server import Server

server = Server("0.0.0.0", 8080)  # Замените адрес и порт по вашим требованиям

@server.event
def on_message(client, message):
    # Обработка входящего сообщения и отправка его другим клиентам
    server.broadcast(message)

server.run()
