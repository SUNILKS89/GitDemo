# import mysql.connector
from Utils.configurations import *

#conn = mysql.connector.connect(host='localhost',database="APIDevelop",user='root',password='root')
conn = get_dbconnection()
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")

row = cursor.fetchone()#data is provided in tuple format
print(row)
print(row[3])
rowAll = cursor.fetchall()#data is provided in list of tuples
print(rowAll)
print(rowAll[0][0])

data = ("UK","Jmeter")
query = "update CustomerInfo set Location =%s where CourseName=%s"
cursor.execute(query,data)
conn.commit()#after writing data to database commit() should be called

query1 = "delete from CustomerInfo where CourseName='Webservices'"
cursor.execute(query1)
conn.commit()

conn.close()