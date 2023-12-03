import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Jigar@2003",
 database="electronics"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE LAPTOP")
print('\nTable Dropped\n')
mydb.commit()
mycursor.execute("DROP DATABASE electronics")
mydb.close()