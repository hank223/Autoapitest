# 1. 导包
import pymysql
# 2. 建立连接，建立连接时要设置自动提交事务开发，并设置为True
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       database='books',
                       autocommit=True,
                       port=3306,
                       charset='utf8')
# 3. 获取游标
cursor = conn.cursor()
# 4. 执行SQL：需求插入一个本书，书名是创新公司，列包括（id，title，pub_date)
insert_sql = "insert into t_book(`id`, `title`, `pub_date`) values(4, '创新公司', '1970-01-01');"
# 增
cursor.execute(insert_sql)
# 改
upset_sql = "update t_book set `read`= `read`+1 where `title`='创新公司';"
cursor.execute(upset_sql)
# 删
delete_sql = "DELETE from t_book where `title` = '创新公司';"
cursor.execute(delete_sql)
# 执行结束之后，可以在navicat里，重新查询，查看执行结果
# 5. 关闭游标
cursor.close()
# 6. 关闭连接
conn.close()