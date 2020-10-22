from tkinter import *
import mysql.connector
from mysql.connector import Error
from validate import validate
from PIL import Image

# def init():
# 	try:
# 		conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
# 		if conn.is_connected():
# 			db_info=conn.get_server_info()
# 			print("Connected to mysql server version: ",db_info)
# 			cursor=conn.cursor()
# 			cursor.execute("create database if not exists expense")
# 			cursor.execute("use expense")
# 			cursor.execute("select database()")
# 			record=cursor.fetchone()
# 			print("you are connected to database",record)
# 			cursor.execute("create table if not exists users (id int(11) not null AUTO_INCREMENT PRIMARY KEY,user_name varchar(255),password varchar(255))")
# 	except:
# 		print("error occured")

# conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
# if conn.is_connected():
# 	db_info=conn.get_server_info()
# 	print("Connected to mysql server version: ",db_info)
# 	cursor=conn.cursor()
# 	cursor.execute("create database if not exists expense")
# 	cursor.execute("use expense")
# 	cursor.execute("select database()")
# 	record=cursor.fetchone()
# 	print("you are connected to database",record)
# 	cursor.execute("create table if not exists users (id int(11) not null AUTO_INCREMENT PRIMARY KEY,user_name varchar(255),password varchar(255))")
# else:
# 	print("Connection Failed!")


# def login_btn():
# 	user=userfld.get()
# 	passw=passwfld.get()
# 	validate(user,passw)

# def register_btn():
# 	window.destroy()
# 	import register

# def validate(user,passw):
# 	cursor.execute("SELECT user_name,password FROM users")
# 	try:
# 		for(usern,passwrd) in cursor:
# 			if user==usern and passw==passwrd:
# 				validate=True
# 			else:
# 				validate=False
# 	except Error as e:
# 		print("Error occured")

# 	if validate==True:
# 		print("Greatt")
# 		window.destroy()
# 		import dashboard
# 	elif validate==False:
# 		print("try again")


	
# add widgets here
window=Tk()
window.title('Expense Tracker')
window.geometry("800x400+10+20")
window.configure(bg='#fff')


#logo
image = PhotoImage(file='images/logo.png')
image = image.subsample(9, 9) # divide by 4
label = Label(image=image, bg="#fff")
label.place(x=60, y=30)

#Username
lbl=Label(window, text="Username:", fg='black',bg='#fff', font=("Verdana", 12))
lbl.place(x=60, y=105)
userfld=Entry(window,width=40,bg='#f7f7f7')
userfld.place(x=63, y=140)
# userfld=Entry(window,width=40,bg='#f7f7f7')
# userfld.grid(row=7,column=3)

#Password
lb2=Label(window, text="Password:", fg='black',bg='#fff', font=("Verdana", 12))
lb2.place(x=60, y=175)
passwfld=Entry(window,width=40,bg='#f7f7f7',show="*")
passwfld.place(x=63, y=210)

#button: Login
# btn1=Button(window,font=("Verdana", 12),highlightthickness = 0,bg='#fff', bd = 0,command=login_btn)
# img = PhotoImage(file="images/signin.png").subsample(3, 3)
# btn1.config(image=img,bg='#fff')
# btn1.place(x=250, y=245)



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
btn1.place(x=250, y=245)

#register
# btn2=Button(window, text="register", fg='blue',font=("Verdana", 12),command=register_btn)
# btn2.place(x=150, y=245)

btn2=Button(window,text="Register",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="#fff",
	command=register_btn)
img2 = PhotoImage(file="images/2.png").subsample(3, 3)
btn2.config(image=img2,bg='#fff')
btn2.place(x=63, y=245)


window.mainloop()