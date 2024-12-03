from guizero import *
from random import *

def gacha():
    ki_tu = ["12e","skd","123d"]
    a = choice(ki_tu)
    b = choice(ki_tu)
    c = choice(ki_tu)
    password = a + b + c
    password_text.value = password

app=App("random password app(easier to hack lol)")
text=Text(app,text= "PUSH THIS BUTTON TO GACHA PASSWORD")
button=PushButton(app,command=gacha,text="PUSH")
password_text=Text(app,text="")
app.display()