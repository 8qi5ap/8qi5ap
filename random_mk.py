import secrets
from guizero import *

def random_password():
    password.value = secrets.token_urlsafe(10)
app=App("RANDOM STRONG PASSWORD")
title=Text(app,"click to random a password")
button=PushButton(app,command=random_password,text="start")
password=Text(app, text="")
picture=Picture(app,image="images/hakari.png")
app.bg="purple"
app.display()

