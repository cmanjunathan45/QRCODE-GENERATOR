import tkinter
from tkinter import *
import tkinter as tk
import pyqrcode
import png
from pyqrcode import QRCode
from datetime import datetime
from PIL import Image,ImageTk
import webbrowser
import os

root=tk.Tk()
root.title("QRCode Generator | Manjunathan")
root.geometry("600x600")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))
root.config(bg="#000000")


label=Label(root,text="Enter the file URL ",bg="#000000",fg="#ffffff",font=("courier",15,"bold italic"))
label.place(x=190,y=15)

urlEntry=Entry(root,fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=40,borderwidth=6)
urlEntry.place(x=50,y=50)

def generate():
	path="QR_CODES/"
	now=datetime.now()
	current_time = now.strftime("%H%M%S")
	url=urlEntry.get()
	file_name="QR_"+current_time
	pyurl=pyqrcode.create(url)

	pyurl.png(path+file_name,scale=8)
	imgLoad = Image.open(path+file_name) 
	imgLoad = imgLoad.resize((200, 200), Image.ANTIALIAS) 
	imgLoad = ImageTk.PhotoImage(imgLoad) 
	panel = Label(root, image = imgLoad) 
	panel.image = imgLoad 
	panel.place(x=190,y=350)

buttonGenerate=Button(root,text="Generate",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=generate)
buttonGenerate.place(x=230,y=100)

buttonClear=Button(root,text="Clear",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=lambda: urlEntry.delete(0,END))
buttonClear.place(x=230,y=160)

buttonExit=Button(root,text="Exit",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=root.destroy)
buttonExit.place(x=230,y=220)

buttonContact=Button(root,text="Contact",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=230,y=280)

root.mainloop()
