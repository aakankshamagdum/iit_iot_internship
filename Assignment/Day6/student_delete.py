
import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "students",
    use_pure = True
)


rollno = int(input("Enter rollno of a student to be deleted : "))

query = f"delete from students where rollno = {rollno};"


cursor = connection.cursor()


cursor.execute(query)


connection.commit()


cursor.close()


connection.close()

