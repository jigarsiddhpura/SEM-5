# import mysql.connector
import sqlite3
import pandas as pd

# connection = mysql.connector.connect(host='localhost',database='jweltags',user='jigar',password='Jigar@2003')

conn = sqlite3.connect('db1.db')  # Reconnect to the database
query = 'SELECT * FROM table1'
result = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display the query result
print(result.head())
