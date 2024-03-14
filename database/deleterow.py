import MySQLdb as ms
# for oracle 
# import cx_Oracle as co

args = int(input("Enter the id"))

conn = ms.connect(host = 'localhost' , database='laravelcourse', user='root', password='abcdefgh')

# Oracle : co.connect("SYSTEM/abcdefgh@")

cursor = conn.cursor() #

sql = "delete from coronas where id = %d"

try:
    cursor.execute(sql % args)
    conn.commit()
    print("one row deleted")
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()


