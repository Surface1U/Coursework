#короче, я тут жёстко прикольнулся и открыл для себя мир библиотек в питоне. 
#Это просто очень сильно облегчило мне задачу, единственное, что я сейчас делаю - это разрабатываю окнонное приложение под программу. Ща ща ща
#Программа на 50 строк. какой ужас хахахаха

from tkinter import *


from Crypto.Cipher import DES

from pygost.gost3410 import CURVES
from os import urandom
from pygost.gost3410 import prv_unmarshal
from pygost.gost3410 import prv_marshal
from pygost.gost3410 import public_key
from pygost.gost3410 import pub_marshal
from pygost.utils import hexenc
from pygost import gost34112012512
from pygost.gost3410 import sign
from pygost.gost3410 import verify


root = Tk()

def btn_click():
    curve = CURVES["id-tc26-gost-3410-12-512-paramSetA"]
    prv_raw = urandom(64)

    prv = prv_unmarshal(prv_raw)
    prv_raw = prv_marshal(curve, prv)
    pub = public_key(curve, prv)

    print("Public key is:", hexenc(pub_marshal(pub)))
    data_for_signing = b"I love Russia"
    dgst = gost34112012512.new(data_for_signing).digest()
    signature = sign(curve, prv, dgst)
    verify(curve, pub, dgst, signature)

    key = b'abcdefgh'

    def pad(text):
        while len(text) % 8 != 0:
            text += b' '
        return text

    des = DES.new(key, DES.MODE_ECB)
    text = b'Python rocks!'
    padded_text = pad(text)

    encrypted_text = des.encrypt(padded_text)
    print(encrypted_text)
    # b'>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'


root['bg']='#fafafa'
root.title('CryptoMachine')
root.wm_attributes('-alpha',0.7)
root.geometry('800x600')

root.resizable(width=False,height=False)

canvas=Canvas(root,height=800,width=600)
canvas.pack()

frame = Frame(root,bg='red')
frame.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.7)

title = Label(frame,text='CryptoMachine',bg='gray',font=40)
title.pack()

btn=Button(frame,text='Generate',bg = 'white',command=btn_click)
btn.pack()


root.mainloop()

