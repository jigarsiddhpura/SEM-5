import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jigar@2003",
    database="electronics"
)
mycursor = mydb.cursor()
sql = """ 
        INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES(%s, %s, %s, %s)
                 """
val = [(26,'Windows','144000','2020-11-23'),(39,'Macbook M2 ','6670000','2012-08-27')]
mycursor.executemany(sql,val)
mydb.commit()