import mysql.connector as myc
from datetime import datetime
connection = myc.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

sensor_id = int(input("Enter sensor_id:"))
moisture_level = int(input("Enter moisture_level:"))

query = f"INSERT INTO soil_moisture(sensor_id,moisture_level,date_time) VALUES({sensor_id},{moisture_level},{datetime.now()}')"

cursor  = connection.cursor()
cursor.execute(query)

connection.commit()

cursor.close()
connection.close()