import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='books', charset='utf8',autocommit=True)
cursor = conn.cursor()
# 插入一本书，书名为‘python从入门到放弃’，阅读量为50，评论量为0，发布日志为：2020-01-01
insert_sql = "insert into t_book(`title`,`pub_date`,`read`,`comment`) values('python从入门到放弃','2020-01-01',50,0);"
cursor.execute(insert_sql)
# 测试工程师人员发现一个bug，这个本书的评论数与实际不符，要求你把评论量修改为修正后的值：250
upset_aql = "update t_book set `comment`=250 where `title`='python从入门到放弃';"
cursor.execute(upset_aql)
# 老板投资了python，觉得这本书名太不吉利，需要下架，请删除这本书。
delete_sql = "delete from t_book where `title`='python从入门到放弃';"
cursor.execute(delete_sql)
# 你删除后，心中不放心到底有没有删除，想确认是否真正删除了，你需要怎么做？
verify_sql = "select `id` from t_book where `title`='python从入门到放弃';"
if cursor.execute(verify_sql) == 0:
    print('查询书籍不存在。')
else:
    print(cursor.execute(verify_sql))

# 5. 关闭游标
cursor.close()
# 6. 关闭连接
conn.close()
