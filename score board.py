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

# b2  =Button(window_1 , text = "muhammad",background="green",fg="yellow")
# b2.pack(side = TOP)
# b3  =Button(window_1 , text = "G3")
# b3.pack(side=RIGHT)
# b11  =Button(window_1 ,text="1",background="black",fg="white",height= 1, width=1,command=printu)
# b11.place(x = 250,y = 250)
# b22  =Button(window_1 , text = "2",background="black",fg="white",height= 1, width=1)
# b22.place(x = 250,y = 280)
# b33  =Button(window_1 , text = "3",background="black",fg="white",height= 1, width=1)
# b33.place(x = 250,y = 310 )
# b44  =Button(window_1 , text = "4",background="black",fg="white",height= 1, width=1)
# b44.place(x = 250,y = 340)
# b5  =Button(window_1 , text = "5",background="black",fg="white",height= 1, width=1)
# b5.place(x = 280,y = 250)
# b6  =Button(window_1 , text = "6",background="black",fg="white",height= 1, width=1)
# b6.place(x = 280,y = 280)
# b7  =Button(window_1 , text = "7",background="black",fg="white",height= 1, width=1)
# b7.place(x = 280,y = 310)
# b8  =Button(window_1 , text = "8",background="black",fg="white",height= 1, width=1)
# b8.place(x = 280,y = 340)
# b9  =Button(window_1 , text = "9",background="black",fg="white",height= 1, width=1)
# b9.place(x = 310,y = 250)
# b10  =Button(window_1 , text = "10",background="black",fg="white",height= 1, width=1)
# b10.place(x = 310,y = 280)
# b11  =Button(window_1 , text = "11",background="black",fg="white",height= 1, width=1)
# b11.place(x = 310,y = 310)
# b12  =Button(window_1 , text = "12",background="black",fg="white",height= 1, width=1)
# b12.place(x = 310,y = 340)
# b13  =Button(window_1 , text = "13",background="black",fg="white",height= 1, width=1)
# b13.place(x = 340,y = 250)
# b14  =Button(window_1 , text = "14",background="black",fg="white",height= 1, width=1)
# b14.place(x = 340,y = 280)
# b15  =Button(window_1 , text = "15",background="black",fg="white",height= 1, width=1)
# b15.place(x = 340,y = 310)
# b16  =Button(window_1 , text = "16",background="black",fg="white",height= 1, width=1)
# b16.place(x = 340,y = 340)




window_1.mainloop()