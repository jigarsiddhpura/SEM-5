import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jigar@2003",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE electronics")
mycursor.execute("use electronics")
mycursor.execute("""
                 CREATE TABLE LAPTOP(
                    Id int(11) NOT NULL,
                    Name varchar(250) NOT NULL,
                    Price float NOT NULL,
                    Purchase_date Date NOT NULL,
                    PRIMARY KEY(Id)
                 )
                 """)
mydb.commit()