import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="n9q8DF1#zX"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
