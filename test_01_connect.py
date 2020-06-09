# 导包
import pymysql
# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books")
# 创建游标对象
cursor = conn.cursor()
# 执行操作：查询数据库版本信息
cursor.execute("select version()")
# 获取查询结果
result = cursor.fetchone()
print("result=", result)
# 关闭游标对象
cursor.close()