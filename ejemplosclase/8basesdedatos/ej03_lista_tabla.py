import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="iesgc",
  password="Ies_GCap_2022",
  database="BankGC"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM CUSTOMERS")
rows = cursor.fetchall()

for row in rows:
  print(row)
