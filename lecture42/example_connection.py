import mysql.connector

# creating the connection object
connection = mysql.connector.connect(
host ="localhost",
user ="root",
password ="n9q8DF1#zX")
# creating cursor object
cursorObj = connection.cursor()
# selecting the database 
cursorObj.execute("USE radiotheaters")
# Fetching a single row 
print("Database selected Successfully...!")
# disconnecting from server
connection.close()