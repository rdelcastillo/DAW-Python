import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="iesgc",
  password="Ies_GCap_2022"
)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")

for db in cursor:
  print(db)
