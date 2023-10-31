from flet.client import Client

client = Client("127.0.0.1", 8080)  # Укажите адрес и порт сервера

@client.event
def on_message(message):
    # Обработка входящего сообщения
    print(message)

client.connect()

while True:
    message = input("Введите сообщение: ")
    client.send(message)
