from pymysql import Connection

conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="061532",
    autocommit=True
)


print(conn.get_server_info())

cursor=conn.cursor()

conn.select_db("test")

cursor.execute("update test.student set id=6 where name='jhl'")

conn.close()

