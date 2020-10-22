from tkinter import *
import mysql.connector
from mysql.connector import Error
from PIL import Image
from datetime import date

conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
cursor=conn.cursor()

if conn.is_connected():
	# cursor.execute("create database if not exists spent")
	cursor.execute("use expense")
	cursor.execute("select database()")
	record=cursor.fetchone()
	print("you are connected to database",record)

	username="spent"
	query="create table if not exists spent (id int(11) not null AUTO_INCREMENT PRIMARY KEY,name varchar(255),amount int(255),category varchar(255),date varchar(10))"
	cursor.execute(query)
else:
	print("Connection Failed!")




dash=Tk()
dash.geometry('800x400')
dash.configure(bg='#fff')
l1=Label(dash,text='Dashboard',font=("Verdana", 12,"bold"),bg="orange",)
l1.grid(row=0,column=0,padx=10, pady=10)

def log():
	name=namefld.get()
	amount=amtfld.get()
	category=catfld.get()
	date = today.strftime("%d/%m/%Y")
	data = ("name","amount","category","date")
    query="insert into spent values (%s,%s,%s,%s)"
    cursor.execute(query,data)
    conn.commit()


    
def showall():
	cursor.execute("SELECT name,amount,category,date FROM spent")
	i=2 
	for spent in cursor: 
    		for j in range(len(spent)):
        		e = Entry(dash,bg='#f7f7f7',fg='blue',width=15,xscrollcommand=10) 
        		e.grid(row=i, column=j) 
        		e.insert(END, spent[j])
        		e.configure()
    		i=i+1


btn1=Button(dash,text="New Expense",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black")
img = PhotoImage(file="images/1.png").subsample(3, 3)
btn1.configure(image=img,bg='#fff')
btn1.place(x=640, y=20)

btn22=Button(dash,text="Show All",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=showall)
img22 = PhotoImage(file="images/2.png").subsample(3, 3)
btn22.configure(image=img22,bg='#fff')
btn22.place(x=640, y=80)




exp_name=Label(dash, text="Name:", fg='black',bg='#fff', font=("Verdana", 12))
exp_name.place(x=450, y=25)
namefld=Entry(dash,width=22,bg='#f7f7f7')
namefld.place(x=454, y=50)


exp_amt=Label(dash, text="Amount:", fg='black',bg='#fff', font=("Verdana", 12))
exp_amt.place(x=450, y=80)
amtfld=Entry(dash,width=22,bg='#f7f7f7')
amtfld.place(x=454, y=105)


exp_cat=Label(dash, text="Category:", fg='black',bg='#fff', font=("Verdana", 12))
exp_cat.place(x=450, y=135)
catfld=Entry(dash,width=22,bg='#f7f7f7')
catfld.place(x=454, y=160)





dash.mainloop()