#create table
import MySQLdb as ms
# for oracle 
# import cx_Oracle as co

conn = ms.connect(host = 'localhost' , database='laravelcourse', user='root', password='abcdefgh')
cursor = conn.cursor()

cursor.execute("drop table if exists emptab")

sql = "create table emptab(eid int, ename char(200), email char(20), salary float)"
cursor.execute(sql)
print("one table created...")
cursor.close()
conn.close()  

