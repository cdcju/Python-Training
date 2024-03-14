import MySQLdb as ms
# for oracle 
# import cx_Oracle as co

conn = ms.connect(host = 'localhost' , database='laravelcourse', user='root', password='abcdefgh')

# Oracle : co.connect("SYSTEM/abcdefgh@")

cursor = conn.cursor() #

str = "insert into coronas (country_name , symptoms, cases, created_at, updated_at ) values ('Pakistan', 'Feaver', 256, '2020-12-28 09:03:49', '2020-12-28 10:59:56')"

try:
    cursor.execute(str)
    print("one row inserted")
    conn.commit()
except:
    conn.rollback()

cursor.close()
conn.close()


