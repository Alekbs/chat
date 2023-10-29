from peewee import *

#указываем базу данных
db = SqliteDatabase('Users.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = dborder_by = 'id'

class User(BaseModel):
    login = CharField()
    password = CharField()
    phone = CharField()
    avatar = CharField() # Разобраться как использовать изображения

    class Meta:
        db_table = 'users'

class Chat(BaseModel):
    id = PrimaryKeyField(unique=True)
    chat_name = CharField()
    chat_logo = CharField() # Изображение
    admin = CharField() # почему-то свзяь идет от сообщения???

    class Meta:
        db_table = 'chats'


class Message(BaseModel):
    id = PrimaryKeyField(unique=True)
    user_from = CharField() # Связь с Users
    user_to = CharField() # Непонятное поле, сообщение должно принадлежать чату
    chat_id = CharField() # Связь с Chats
    message = CharField() #Текст сообщения
    date_created = DateField()
    is_read = BooleanField() 

    class Meta:
        db_table = 'messages'


class UserChatLink(BaseModel):
    user_id = ForeignKeyField(User)
    chat_id = ForeignKeyField(Chat)

    class Meta:
        db_table = "user_chat_links"
