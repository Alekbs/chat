from models import *

with db:
    db.create_tables([User, Chat, Message, UserChatLink])

print("Done")

