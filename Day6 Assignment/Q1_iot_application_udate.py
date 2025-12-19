import mysql.connector as myc
from datetime import datetime
connection = myc.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensors",
    use_pure = True
)
id = int(input("Enter id whose temperature to be updated:"))
temperature = int(input("Enter new temperature:"))

query = f"UPDATE sensors SET temperature = {temperature} WHERE ID = {id}; "

cursor = connection.cursor()


cursor.execute(query)

connection.commit()

cursor.close()

connection.close()