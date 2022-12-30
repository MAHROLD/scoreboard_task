import time
from tkinter import *

def printu():
    print("muhammad")
def timesnow():
    currentime = time.strftime ("%H:%M:%S")
    timelabel.config (text=currentime)

    timelabel.after(1000, timesnow)
global x
x=0
global y
y=0

def mar():
	global x
	x=x+1
	label_1  =Label(window_1 , text = (x),bd='5',width=8,height=2)
	label_1.place(x=70,y=80)
	
def cro():
	global y
	y=y+1
	label_2  =Label(window_1 , text = (y),bd='5',width=8,height=2)
	label_2.place(x=260,y=80)
	
window_1=Tk()
window_1.geometry('400x400')
# label_1= Label(window_1 , text = "lol")
# label_1.place(x=240,y=240)
timelabel = Label(window_1, font=("Courier", 44))

timelabel.grid()
timelabel.place(x=60,y=0)
timesnow()
photo_1 = PhotoImage(file='moroco.png')
photo_1 = photo_1.subsample(8,8)
photo_2 = PhotoImage(file='coratia.png')
photo_2 = photo_2.subsample(8,8)
b1  =Button(window_1 ,text="iti",image=photo_1,height=90,width=90,command=cro)
b1.place(x=240,y=120)
b1e  =Button(window_1 ,text="iti",image=photo_2,height=90,width=90,command=mar)
b1e.place(x=70,y=120)
label_1  =Label(window_1 , text = (x),bd='5',width=8,height=2)
label_1.place(x=70,y=80)
label_2  =Label(window_1 , text = (y),bd='5',width=8,height=2)
label_2.place(x=260,y=80)

window_1.mainloop()
