import MySQLdb as ms
# for oracle 
# import cx_Oracle as co

args = int(input("Enter the id"))
cases = int(input("Enter the cases"))
print("Two variables are %d and %d" % (args, cases)) #note

conn = ms.connect(host = 'localhost' , database='laravelcourse', user='root', password='abcdefgh')

# Oracle : co.connect("SYSTEM/abcdefgh@")

cursor = conn.cursor() #

sql = "update coronas set cases = %d where id = %d"

try:
    cursor.execute(sql % (cases, args))
    conn.commit()
    print("one row updated")
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()