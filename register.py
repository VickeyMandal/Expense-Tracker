from tkinter import *
from tkinter.messagebox import showinfo,showerror
import mysql.connector

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
            # reg_window.destroy()# now close form window

        copyri8 = Label(reg_window,text='Designed and developed by: Bappaditya Mandal',bg='powder blue')
        copyri8.pack(side=BOTTOM,pady=3)    

reg_window = Tk()
reg_window.title("Registration")
reg_window.geometry('800x400')
reg_window.config(bg='#fff')
# formName = Label(reg_window,text='New User Registration',fg='black',font=("Verdana", 12))
# formName.pack()

L1 = Label(reg_window,text='User Name*',fg='black',font=("Verdana", 12))
L1.place(x=30,y=100)
regUser=Entry(reg_window)
regUser.place(x=140,y=100)
#       Get user password ========================
L3 = Label(reg_window,text='Enter Password*',fg='black',font=("Verdana", 12))
L3.place(x=30,y=160)
regPass = Entry(reg_window)
regPass.place(x=140,y=160)
#       confirm password==========================
L4 = Label(reg_window,text='Confirm Password*',fg='black',font=("Verdana", 12))
L4.place(x=30,y=185)
confirm = Entry(reg_window)
confirm.place(x=140,y=185)

submit = Button(reg_window,text='Register',fg='white',bg='green',width=30,command=register)
submit.place(x=200,y=200)



        
        
reg_window.mainloop()