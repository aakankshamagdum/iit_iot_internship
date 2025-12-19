import mysql.connector as myc

connection = myc.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

query ="SELECT * FROM soil_moisture;"
query1 ="SELECT * FROM soil_moisture WHERE sensor_id < 150";


cursor  = connection.cursor()

cursor.execute(query)

readings = cursor.fetchall()

print(readings)

cursor.execute(query1)

filtered_readings = cursor.fetchall()

print(filtered_readings)

cursor.close()

connection.close()