from models import *


with db:
    users = User.get()
print(users.login, users.password)
print("Done")

