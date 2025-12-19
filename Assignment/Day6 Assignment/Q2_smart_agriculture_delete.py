import mysql.connector as myc

connection = myc.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

sensor_id = int(input("Enter sensor_id to be deleted:"))

query = f"DELETE FROM soil_moisture WHERE sensor_id = {sensor_id};"

cursor  = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()