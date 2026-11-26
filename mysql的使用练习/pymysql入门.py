from pymysql import Connection
conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
#print(conn.get_server_info())
cursor=conn.cursor()#获取游标对象
conn.select_db("test")#选择数据库
cursor.execute("create table test_pymysql(id int)")

