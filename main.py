from tkinter import *
import mysql.connector
from mysql.connector import Error
from validate import validate
from PIL import Image


window=Tk()
window.title('Expense Tracker')
window.geometry("420x400")
window.configure(bg='#fff')
logo = PhotoImage(file = 'images/logo.png') 
window.iconphoto(False, logo)

#logo
image = PhotoImage(file='images/logo.png')
image = image.subsample(5, 5) # divide by 4
label = Label(image=image, bg="#fff")
label.place(x=165, y=30)

#Username
lbl=Label(window, text="Username:", fg='black',bg='#fff', font=("Verdana", 12))
lbl.place(x=60, y=145)
userfld=Entry(window,width=49,bg='#f7f7f7')
userfld.place(x=63, y=180)
# userfld=Entry(window,width=40,bg='#f7f7f7')
# userfld.grid(row=7,column=3)

#Password
lb2=Label(window, text="Password:", fg='black',bg='#fff', font=("Verdana", 12))
lb2.place(x=60, y=215)
passwfld=Entry(window,width=49,bg='#f7f7f7',show="*")
passwfld.place(x=63, y=250)





def login_btn():
	user= userfld.get()
	passw= passwfld.get()
	# os.system('validate.py')
	
	if validate(user,passw):
		window.destroy()
		import dashboard
	else:
		window.destroy()

	

def register_btn():
	window.destroy()
	import register



btn1=Button(window,text="Sign in",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=login_btn)
img = PhotoImage(file="images/1.png").subsample(3, 3)
btn1.config(image=img,bg='#fff')
btn1.place(x=220, y=300)


btn2=Button(window,text="Register",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="#fff",
	command=register_btn)
img2 = PhotoImage(file="images/2.png").subsample(3, 3)
btn2.config(image=img2,bg='#fff')
btn2.place(x=63, y=300)


window.mainloop()