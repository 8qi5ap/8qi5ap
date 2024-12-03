from guizero import *
from random import *

names = ["pho","bun bo","com tam","chan ga sot thai","bò wagu","banh kem","ba chỉ","cainit"]


def choose_food():
    name = choice(names)
    name_text.value = name 

app=App("menu", bg="white")

title=Text(app,"nhấn vào để random food")
button=PushButton(app,command=choose_food,text="bắt đầu gacha")
button.bg= "white"
button.text_size=20
name_text=Text(app,text="")
app.display()

# EM CHƯA THÊM HÌNH VÀO ĐC