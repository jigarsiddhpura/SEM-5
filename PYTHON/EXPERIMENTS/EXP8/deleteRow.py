import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jigar@2003",
    database="electronics"
)
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM Laptop WHERE Id = 15")
mydb.commit()
res = mycursor.fetchall()
for x in res:
    print(x)