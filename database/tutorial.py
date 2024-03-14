import MySQLdb as ms
# for oracle 
# import cx_Oracle as co

conn = ms.connect(host = 'localhost' , database='laravelcourse', user='root', password='abcdefgh')

# Oracle : co.connect("SYSTEM/abcdefgh@")

cursor = conn.cursor() #

cursor.execute("select * from coronas")

print("the total number of rows: {}".format(cursor.rowcount))

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()    