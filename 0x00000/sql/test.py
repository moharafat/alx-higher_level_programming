import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123pawword"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)