import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="iesgc",
  password="Ies_GCap_2022",
  database="BankGC"
)

cursor = mydb.cursor()

cursor.execute("SHOW TABLES")

for table in cursor:
  print(table)
