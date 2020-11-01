from tkinter import *
from tkinter import ttk 
import mysql.connector
from mysql.connector import Error
from PIL import Image
from datetime import date
from tkinter import messagebox
from addexpense import addpop


#-------------------DATABASE CONNECTION-------------------#

conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
cursor=conn.cursor()

if conn.is_connected():
	cursor.execute("use expense")
	cursor.execute("select database()")
	record=cursor.fetchone()
	print("you are connected to database",record)

	username="spent"
	query="create table if not exists spent (id int(11) not null AUTO_INCREMENT PRIMARY KEY,name varchar(255),amount int(255),category varchar(255),date varchar(10))"
	cursor.execute(query)
else:
	print("Connection Failed!")


#Initializing window of the program and its attributes

dash=Tk()
dash.geometry('800x400')
dash.configure(bg='#fff')
dash.title("Dashboard - Expense Tracker")
logo = PhotoImage(file = 'images/logo.png') 
dash.iconphoto(False, logo)



#-------------------LABELS-------------------#

l1=Label(dash,text='Records',font=("Verdana", 12,"bold"),bg="orange",)
l1.grid(ipadx=4)
n=Label(dash, text="Name",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=0,padx=20)
a=Label(dash, text="Amount",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=1,padx=20)
c=Label(dash, text="Category",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=2,padx=20)
d=Label(dash, text="Date",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=3,padx=20)


# total spent label
ttlspent=Label(dash, text="Total Spent:",width=15, fg='black',bg='orange', font=("Verdana", 12))
ttlspent.place(x=495, y=140)

# category label
exp_cat2=Label(dash, text="By Category:", fg='black',bg='#fff', font=("Verdana", 12))
exp_cat2.place(x=490, y=170)

#-------------------FUNCTIONS-------------------#

# Showall button function & display every item in table
def showall():
		clear()
		data = readfromdatabase()
		for index, dat in enumerate(data):
					          	Label(dash, text=dat[1],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=0,padx=20)
					          	Label(dash, text=dat[2],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=1,padx=20)
					          	Label(dash, text=dat[3],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=2,padx=20)
					          	Label(dash, text=dat[4],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=3,padx=20)


# Fetches data from Tables Spent
def readfromdatabase():
    cursor.execute("SELECT * FROM spent limit 0,15")
    return cursor.fetchall()

# Fetches to total amount spent
def showtotal():
	my_str = StringVar()
	label2 = Label(dash,  textvariable=my_str, width=11,fg='red', font=("Verdana", 12) )  
	label2.place(x=660, y=140) 
	cursor.execute("select sum(amount) from spent")
	ttl = cursor.fetchone()
	my_str.set(ttl)
	
# Displays category items
def showbycategory():
	data = showby()
	for index, dat in enumerate(data):
					        Label(dash, text=dat[1],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=0,padx=20)
					        Label(dash, text=dat[2],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=1,padx=20)
					        Label(dash, text=dat[3],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=2,padx=20)
					        Label(dash, text=dat[4],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=3,padx=20)

# clears the table displayed
def clear():
	data = readfromdatabase()
	
	for index, dat in enumerate(data):
					        Label(dash, text="                        ",bg='#fff',).grid(row=index+3, column=0,padx=20)
					        Label(dash, text="        ",bg='#fff',).grid(row=index+3, column=1,padx=20)
					        Label(dash, text="                      ",bg='#fff',).grid(row=index+3, column=2,padx=20)
					        Label(dash, text="                      ",bg='#fff',).grid(row=index+3, column=3,padx=20)

# Fetches to total amount spent by category
def categorysum():

	my_str = StringVar()
	label2 = Label(dash,  textvariable=my_str, width=11,fg='red', font=("Verdana", 12) )  
	label2.place(x=660, y=140) 
	cate=catfld1.get()
	cursor.execute("select sum(amount) FROM spent where category='{}'".format(cate))
	ttl = cursor.fetchone()
	my_str.set(ttl)


# selects category and fetches category info
def showby():
	clear()
	categorysum()
	cate=catfld1.get()
	qq="SELECT * FROM spent where category='{}'".format(cate)
	cursor.execute(qq)
	return cursor.fetchall()







#-------------------DASHBOARD BUTTON-------------------#

# Add expense button
btn1=Button(dash,text="Add Expense",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=addpop)
img = PhotoImage(file="images/1.png").subsample(3, 3)
btn1.configure(image=img,bg='#fff')
btn1.place(x=640, y=20)

# showall button
btn22=Button(dash,text="Show All",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=showall)
img22 = PhotoImage(file="images/2.png").subsample(3, 3)
btn22.configure(image=img22,bg='#fff')
btn22.place(x=490, y=80)

# total spent button
btn_total=Button(dash,text="Total Spent",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=showtotal)
btn_total.configure(image=img22,bg='#fff')
btn_total.place(x=640, y=80)



#  category combobox
ca = StringVar() 
catfld1 = ttk.Combobox(dash, width = 27, textvariable = ca)
catfld1['values'] = ('Appliances',  
                          'Garments', 
                          'Food', 
                          'Essentials',
                          'Electrionics',
                          'Home',
                          'Travel',
                          'Stationery',
                          'Misc')

catfld1.place(x=495, y=200)

# show button
btn3=Button(dash,text="Show",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=showbycategory)
img3 = PhotoImage(file="images/2.png").subsample(3, 3)
btn3.configure(image=img3,bg='#fff')
btn3.place(x=490, y=230)



dash.mainloop()