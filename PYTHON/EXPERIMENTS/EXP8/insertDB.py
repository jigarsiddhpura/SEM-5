import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jigar@2003",
    database="electronics"
)
mycursor = mydb.cursor()
# mycursor.execute("use electronics")
mycursor.execute(""" 
                 INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES(15,'Acer aspire 7','52000','2019-08-17')
                 """)
mydb.commit()
print("hello")