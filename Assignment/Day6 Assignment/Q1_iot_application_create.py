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
id = int(input("Enter id:"))
temperature = float(input("Enter temperature:"))
humidity = float(input("Enter humidity:"))

query = f"INSERT INTO sensors(id,temperature,humidity,timestamp) VALUES({id},{temperature},{humidity},'{datetime.now()}')"

cursor  = connection.cursor()
cursor.execute(query)

connection.commit()

cursor.close()
connection.close()