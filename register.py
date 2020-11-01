from tkinter import *
from tkinter.messagebox import showinfo,showerror
import mysql.connector
from tkinter import ttk 
import mysql.connector
from mysql.connector import Error
from PIL import Image
from datetime import date
from tkinter import messagebox

#Initializing window of the program and its attributes

reg_window = Tk()
reg_window.title("Registration - Expense Tracker")
reg_window.geometry("415x400")
reg_window.config(bg='#fff')
logo = PhotoImage(file = 'images/logo.png') 
reg_window.iconphoto(False, logo)


#logo
image = PhotoImage(file='images/logo.png')
image = image.subsample(5, 5) # divide by 4
label = Label(image=image, bg="#fff")
label.place(x=170, y=30)



#-------------------DATABASE CONNECTION-------------------#

conn = mysql.connector.connect(host = "localhost",database="expense", user = "root" , passwd = "2812" )
if conn.is_connected():
    db_info=conn.get_server_info()
    print("Connected to mysql server version: ",db_info)
    cursor=conn.cursor()
    cursor.execute("create database if not exists expense")
    cursor.execute("select database()")
    record=cursor.fetchone()
    print("you are connected to database",record)
    cursor.execute("create table if not exists users (id int(11) not null AUTO_INCREMENT PRIMARY KEY,user_name varchar(255),password varchar(255))")



#-------------------FUNCTIONS-------------------#

# Signin Button function
def back():
    reg_window.destroy()
    import main
 
# Register Button function
def register():
    usr = regUser.get()
    passw,cpassw = regPass.get(),confirm.get()
    if len(usr)==0 or len(passw)==0:
        showerror('All fields required','All fields are required to fill.')
    elif len(passw)<5:
        showinfo('Warning','Password must be atleast 5 character long')
    elif passw!=cpassw:
        showerror('password mismatch','Password Mismatched.')
    else:
                #print(e,p)
        try:
            query = "INSERT INTO users (user_name, password) VALUES (%s,%s )"
            val= (usr,passw)
            cursor.execute(query,val)
            conn.commit()  # to make changes in db
                    
        except Exception as e:
            print(e,'\nThere is an error in registering')
        else:
            print(cursor.rowcount,' record inserted')    
            print(usr,' You are Registered Successfully!')
            showinfo('registered','you are registered Successfully \n %s'%usr)
            cursor.close()
            conn.close()
            
#-------------------LABELS-------------------#

# Get user Name
L1 = Label(reg_window,text='User Name*',fg='black',bg='#fff',font=("Verdana", 12))
L1.place(x=50,y=170)
regUser=Entry(reg_window,bg="#f7f7f7",width=22)
regUser.place(x=220,y=170)

# Get user password
L3 = Label(reg_window,text='Enter Password*',fg='black',bg='#fff',font=("Verdana", 12))
L3.place(x=50,y=200)
regPass = Entry(reg_window,bg="#f7f7f7",width=22)
regPass.place(x=220,y=200)

# confirm passworD
L4 = Label(reg_window,text='Confirm Password*',fg='black',bg='#fff',font=("Verdana", 12))
L4.place(x=50,y=230)
confirm = Entry(reg_window,bg="#f7f7f7",width=22)
confirm.place(x=220,y=230)

#-------------------BUTTONS-------------------#

# Submit Button
submit = Button(reg_window,text='Register',compound=CENTER,font=("Verdana", 12,"bold"),fg='#fff',bd = 0,activeforeground="black",command=register)
img2 = PhotoImage(file="images/2.png").subsample(3, 3)
submit.configure(image=img2,bg='#fff')
submit.place(x=220,y=270)

# Signin Button
back = Button(reg_window,text='Sign In',compound=CENTER,font=("Verdana", 12,"bold"),fg='#fff',bd = 0,activeforeground="black",command=back)
img1 = PhotoImage(file="images/1.png").subsample(3, 3)
back.configure(image=img1,bg='#fff')
back.place(x=50,y=270)

       
reg_window.mainloop()