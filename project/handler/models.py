from peewee import *

# указываем базу данных
db = SqliteDatabase("C:/Users/aleks/Documents/pyth/chat/project/handler/chat.db")


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        dborder_by = "id"


class User(BaseModel):
    login = CharField()
    password = CharField()
    phone = CharField()
    avatar = CharField()  # Разобраться как использовать изображения

    class Meta:
        db_table = "users"


class Chat(BaseModel):
    id = PrimaryKeyField(unique=True)
    chat_name = CharField()
    chat_logo = CharField()  # Изображение
    admin = CharField()  # почему-то свзяь идет от сообщения???

    class Meta:
        db_table = "chats"


class Message(BaseModel):
    id = PrimaryKeyField(unique=True)
    user_from = CharField()
    user_to = CharField()  # Непонятное поле, сообщение должно принадлежать чату
    chat_id = CharField()
    message = CharField()
    date_created = DateField()
    is_read = BooleanField()

    class Meta:
        db_table = "messages"


class UserChatLink(BaseModel):
    user_id = ForeignKeyField(User)
    chat_id = ForeignKeyField(Chat)
    chat_name = ForeignKeyField(Chat)
    chat_logo = ForeignKeyField(Chat)
    last_msg = CharField()
    unread_msg_count = IntegerField()

    class Meta:
        db_table = "user_chat_links"
