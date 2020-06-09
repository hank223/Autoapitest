import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='books',charset='utf8')

cursor = conn.cursor()

cursor.execute("select `id`,`title`,`pub_date`,`read`,`comment` from t_book;")

print('有几本书：',cursor.rowcount)

print("第一本书是：",cursor.fetchmany(2))
print("全部书：",cursor.fetchall())

cursor.close()

conn.close()