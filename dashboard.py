from tkinter import *
from tkinter import ttk 
import mysql.connector
from mysql.connector import Error
from PIL import Image
from datetime import date
from tkinter import messagebox

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
dash.title("Dashboard - Expense Tracker")
logo = PhotoImage(file = 'images/logo.png') 
dash.iconphoto(False, logo)

l1=Label(dash,text='Records',font=("Verdana", 12,"bold"),bg="orange",)
l1.grid(ipadx=4)


n=Label(dash, text="Name",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=0,padx=20)
a=Label(dash, text="Amount",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=1,padx=20)
c=Label(dash, text="Category",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=2,padx=20)
d=Label(dash, text="Date",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=3,padx=20)


def addpop():

	addroot = Tk()
	addroot.geometry('250x250')
	addroot.title("Add Expense")
	addroot.configure(bg='#fff')



	def log():

		try:
			name1=namefld.get()
			amount1=amtfld.get()
			category1=catfld.get()
			date1 = str(date.today())
			val = (name1,amount1,category1,date1)	   
			query1 = "insert into spent VALUES (id,%s,%s,%s,%s)"
			cursor.execute(query1,val)
			conn.commit()
			messagebox.showinfo("showinfo", "Entered succesfully")
			addroot.destroy()
		except Error as e:
			messagebox.showinfo("showerror", "Error occured")


	def closepop():
		addroot.destroy()
	

	exp_name=Label(addroot, text="Name:", fg='black',bg='#fff', font=("Verdana", 12))
	exp_name.place(x=20, y=25)
	namefld=Entry(addroot,width=22,bg='#f7f7f7')
	namefld.place(x=24, y=50)


	exp_amt=Label(addroot, text="Amount:", fg='black',bg='#fff', font=("Verdana", 12))
	exp_amt.place(x=20, y=80)
	amtfld=Entry(addroot,width=22,bg='#f7f7f7')
	amtfld.place(x=24, y=105)


	exp_cat=Label(addroot, text="Category:", fg='black',bg='#fff', font=("Verdana", 12))
	exp_cat.place(x=20, y=135)
	n = StringVar() 
	catfld = ttk.Combobox(addroot, width = 27, textvariable = n)
	catfld['values'] = ('Appliances',  
                          'Garments', 
                          'Food', 
                          'Essentials',
                          'Electrionics',
                          'Home',
                          'Travel',
                          'Stationery',
                          'Misc')

	catfld.place(x=24, y=160)


	add=Button(addroot,text="Add",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=log)
	add.configure(bg='orange')
	add.place(x=20, y=200)


	close=Button(addroot,text="close",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=closepop)
	close.configure(bg='red')
	close.place(x=80, y=200)



def showall():
		clear()
		data = readfromdatabase()
		for index, dat in enumerate(data):
					          	Label(dash, text=dat[1],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=0,padx=20)
					          	Label(dash, text=dat[2],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=1,padx=20)
					          	Label(dash, text=dat[3],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=2,padx=20)
					          	Label(dash, text=dat[4],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=3,padx=20)



def readfromdatabase():
    cursor.execute("SELECT * FROM spent limit 0,15")
    return cursor.fetchall()


def showtotal():
	my_str = StringVar()
	# add one Label 
	label2 = Label(dash,  textvariable=my_str, width=11,fg='red', font=("Verdana", 12) )  
	label2.place(x=660, y=140) 

	# my_str.set("Output")

	cursor.execute("select sum(amount) from spent")
	ttl = cursor.fetchone()
	my_str.set(ttl)
	# print(ttl)
    

def showbycategory():
	data = showby()
	for index, dat in enumerate(data):
					        Label(dash, text=dat[1],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=0,padx=20)
					        Label(dash, text=dat[2],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=1,padx=20)
					        Label(dash, text=dat[3],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=2,padx=20)
					        Label(dash, text=dat[4],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=3,padx=20)


def clear():
	data = readfromdatabase()
	
	for index, dat in enumerate(data):
					        Label(dash, text="                        ",bg='#fff',).grid(row=index+3, column=0,padx=20)
					        Label(dash, text="        ",bg='#fff',).grid(row=index+3, column=1,padx=20)
					        Label(dash, text="                      ",bg='#fff',).grid(row=index+3, column=2,padx=20)
					        Label(dash, text="                      ",bg='#fff',).grid(row=index+3, column=3,padx=20)


def categorysum():

	my_str = StringVar()
	# add one Label 

	label2 = Label(dash,  textvariable=my_str, width=11,fg='red', font=("Verdana", 12) )  
	label2.place(x=660, y=140) 

	# my_str.set("Output")
	cate=catfld1.get()
	cursor.execute("select sum(amount) FROM spent where category='{}'".format(cate))
	ttl = cursor.fetchone()
	my_str.set(ttl)



def showby():
	clear()
	categorysum()
	cate=catfld1.get()
	qq="SELECT * FROM spent where category='{}'".format(cate)
	cursor.execute(qq)
	return cursor.fetchall()




btn1=Button(dash,text="Add Expense",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=addpop)
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
btn22.place(x=490, y=80)


btn_total=Button(dash,text="Total Spent",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=showtotal)
# img22 = PhotoImage(file="images/2.png").subsample(3, 3)
btn_total.configure(image=img22,bg='#fff')
btn_total.place(x=640, y=80)


ttlspent=Label(dash, text="Total Spent:",width=15, fg='black',bg='orange', font=("Verdana", 12))
ttlspent.place(x=495, y=140)





exp_cat2=Label(dash, text="By Category:", fg='black',bg='#fff', font=("Verdana", 12))
exp_cat2.place(x=490, y=170)
	# catfld=Entry(addroot,width=22,bg='#f7f7f7')
	# catfld.place(x=24, y=160)
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