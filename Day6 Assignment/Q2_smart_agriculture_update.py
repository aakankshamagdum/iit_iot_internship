import mysql.connector as myc

connection = myc.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

id =int(input("Enter sensor_id whose moisture_level to be updated:"))
moisture_level =int(input("Enter new moisture_level:"))
query = f"UPDATE soil_moisture SET moisture_level = {moisture_level}WHERE sensor_id ={id};"

cursor  = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()