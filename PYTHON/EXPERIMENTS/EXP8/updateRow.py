import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jigar@2003",
    database="electronics"
)
mycursor = mydb.cursor()
print("Eariler Records : ")
mycursor.execute("SELECT * FROM Laptop")
res = mycursor.fetchall()
for x in res:
    print(x)
mycursor.execute("UPDATE Laptop SET Price = 150000 WHERE Id = 39")
mydb.commit()
print("Updated Records : ")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Laptop")
res = mycursor.fetchall()
for x in res:
    print(x)