import mysql.connector as myc

connection = myc.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensors",
    use_pure = True
)

id = int(input("Enter id to be deleted:"))

query =f"DELETE FROM sensors WHERE id = {id};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()