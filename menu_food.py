from guizero import *
from random import *

images = ["pho.png","bun_bo.png","com_tam.png","chan_ga.png","wagu.png","banh_kem.png","thit_ba_chi.png","cainit.png"]
name = ["pho","bun bo","com tam","chan ga sot thai giam","wagu.png","banh kem","thit ba chi","co cai nit :>"]

def choose_food():
    image = choice(images)
    image_image.value = image

app=App("menu", bg="white")

title=Text(app,"nhấn vào để random food")
button=PushButton(app,command=choose_food,text="bắt đầu gacha")
button.bg= "white"
button.text_size=20
image_image=Picture(app,image="")

app.display()
