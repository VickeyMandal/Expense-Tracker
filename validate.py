import mysql.connector
from mysql.connector import Error

#-------------------DATABASE CONNECTION-------------------#

conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
if conn.is_connected():
	db_info=conn.get_server_info()
	print("Connected to mysql server version: ",db_info)
	cursor=conn.cursor()
	cursor.execute("create database if not exists expense")
	cursor.execute("use expense")
	cursor.execute("select database()")
	record=cursor.fetchone()
	print("you are connected to database",record)
	cursor.execute("create table if not exists users (id int(11) not null AUTO_INCREMENT PRIMARY KEY,user_name varchar(255),password varchar(255))")
else:
	print("Connection Failed!")


#-------------------FUNCTIONS-------------------#

def validate(user,passw):

	cursor.execute("SELECT user_name,password FROM users")
	try:
		for(usern,passwrd) in cursor:
			if user==usern and passw==passwrd:
				return True
			else:
				return False
	except Error as e:
		print("Error occured")



