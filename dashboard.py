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

l1=Label(dash,text='Recent',font=("Verdana", 12,"bold"),bg="orange",)
l1.grid(row=0,column=0)

# def log():
# 			name1=namefld.get()
# 			amount1=amtfld.get()
# 			category1=catfld.get()
# 			date1 = today.strftime("%d/%m/%Y")
# 			data = (id,"Keyboard",1500,"Computer","21/10/2020")
# 		    # query="insert into spent values (%s,%s,%s,%s)"		
# 		    query1 = "insert into spent VALUES (%s,%s,%s,%s,%s)"
# 		    cursor.execute(query1,data)


def log():
	try:
		name1=namefld.get()
		amount1=amtfld.get()
		category1=catfld.get()
		date1 = str(date.today())
		val = (name1,amount1,category1,date1)
			    # query="insert into spent values (%s,%s,%s,%s)"		
		query1 = "insert into spent VALUES (id,%s,%s,%s,%s)"
		cursor.execute(query1,val)
		conn.commit()
		print("Entered succesfully")
	except Error as e:
		print("Error occured")


# def showall():
# 	cursor.execute("SELECT name,amount,category,date FROM spent")
# 	i=2 
# 	for spent in cursor: 
#     		for j in range(len(spent)):
#         		e = Entry(dash,bg='#f7f7f7',fg='blue',width=15) 
#         		e.grid(row=i, column=j) 
#         		e.insert(END, spent[j])
#         		e.configure()
#     		i=i+1



# def showall():
# 		data = readfromdatabase()
# 		for index, dat in enumerate(data):
# 					          	Label(dash, text=dat[0],bg='#fff', font=("Verdana", 8)).grid(row=index+1, column=0,padx=20)
# 					          	Label(dash, text=dat[1],bg='#fff', font=("Verdana", 8)).grid(row=index+1, column=1,padx=20)
# 					          	Label(dash, text=dat[2],bg='#fff', font=("Verdana", 8)).grid(row=index+1, column=2,padx=20)
# 					          	Label(dash, text=dat[3],bg='#fff', font=("Verdana", 8)).grid(row=index+1, column=3,padx=20)



def showall():
		data = readfromdatabase()
		Label(dash, text="Name",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=0,padx=20)
		Label(dash, text="Amount",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=1,padx=20)
		Label(dash, text="Category",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=2,padx=20)
		Label(dash, text="Date",bg='#fff', font=("Verdana", 8,"bold")).grid(row=2, column=3,padx=20)

		for index, dat in enumerate(data):
					          	Label(dash, text=dat[1],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=0,padx=20)
					          	Label(dash, text=dat[2],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=1,padx=20)
					          	Label(dash, text=dat[3],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=2,padx=20)
					          	Label(dash, text=dat[4],bg='#fff', font=("Verdana", 8)).grid(row=index+3, column=3,padx=20)







def readfromdatabase():
    cursor.execute("SELECT * FROM spent limit 0,10")
    return cursor.fetchall()


def showtotal():
	my_str = StringVar()
	# add one Label 
	label2 = Label(dash,  textvariable=my_str, width=19,fg='red' )  
	label2.place(x=454,y=215) 

	# my_str.set("Output")

	cursor.execute("select sum(amount) from spent")
	ttl = cursor.fetchone()
	my_str.set(ttl)
	# print(ttl)
    






btn1=Button(dash,text="Add Expense",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=log)
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


btn_total=Button(dash,text="Total Spent",
	compound=CENTER,font=("Verdana", 12,"bold"),
	fg='#fff',
	bd = 0,
	activeforeground="black",
	command=showtotal)
# img22 = PhotoImage(file="images/2.png").subsample(3, 3)
btn_total.configure(image=img22,bg='#fff')
btn_total.place(x=640, y=140)




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

ttlspent=Label(dash, text="Total Spent:", fg='black',bg='#fff', font=("Verdana", 12))
ttlspent.place(x=450, y=190)



dash.mainloop()