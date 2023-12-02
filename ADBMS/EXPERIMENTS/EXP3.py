import pandas as pd 
import sqlite3

csv_file = './dataset/db2.csv'
df = pd.read_csv(csv_file)

db_file = 'db2.db'
conn = sqlite3.connect(db_file)

table_name = 'table2'
df.to_sql(table_name,conn,if_exists='replace',index=False)

conn.commit()
conn.close()