from tkinter import *
from tkinter import ttk 
import mysql.connector
from mysql.connector import Error
from PIL import Image
from datetime import date
from tkinter import messagebox

#-------------------DATABASE CONNECTION-------------------#

conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
cursor=conn.cursor()
cursor.execute("use expense")

#-------------------MAIN FUNCTION-------------------#

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



#-------------------LABELS-------------------#

	exp_name=Label(addroot, text="Name:", fg='black',bg='#fff', font=("Verdana", 12))
	exp_name.place(x=20, y=25)
	namefld=Entry(addroot,width=22,bg='#f7f7f7')
	namefld.place(x=24, y=50)


	exp_amt=Label(addroot, text="Amount:", fg='black',bg='#fff', font=("Verdana", 12))
	exp_amt.place(x=20, y=80)
	amtfld=Entry(addroot,width=22,bg='#f7f7f7')
	amtfld.place(x=24, y=105)


#-------------------COMBOBOX-------------------#

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


#-------------------BUTTONS-------------------#
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