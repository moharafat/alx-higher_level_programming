import MySQLdb
mydb = MySQLdb.connect(
    host="localhost",
    user="mohamed",
    password="MY_PASS",
    db="ahmedzdatabase"
)
cur = mydb.cursor()
cur.execute("SHOW DATABASES")
for db in cur:
    print(db)