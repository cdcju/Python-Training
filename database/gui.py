from tkinter import *
import MySQLdb as ms

root = Tk()
root.title('Database...')
def update_coronas():
    conn = ms.connect(host = 'localhost' , database='laravelcourse', user='root', password='abcdefgh')
    cursor = conn.cursor() #
    sql = "update coronas set cases = 4560 where id = 7"
    try:
        cursor.execute(sql)
        conn.commit()
        print("one row updated")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


f = Frame(root, height="350" , width = "600")
f.pack()
openBtn = Button(root, text='Update', command=update_coronas)
openBtn.pack(expand=FALSE)
root.mainloop()
