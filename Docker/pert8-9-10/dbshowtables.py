import mysql.connector

mydb = mysql.connector.connect(
    host="0.0.0.0",
    port=23306,
    user="root",
    password="p455w0rd",
    database="basis_data"
)

db = mydb.cursor()

db.execute("SHOW TABLES")

for x in db:
    print(x)
