import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='books', charset='utf8',autocommit=True)
cursor = conn.cursor()
# 1).在“books”数据库中，新增评论表t_comment，包含字段：主键、图书id、评论人名称、评论内容、评论时间。
creat_sql = "CREATE TABLE IF NOT EXISTS `t_comment`" \
            "(`id` int(11) NOT NULL,`comment_name` varchar(255) DEFAULT NULL,`comment_content` varchar(255) DEFAULT NULL," \
            "`comment_time` date DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;"
cursor.execute(creat_sql)
# 2).在评论表中新增一条数据，并更新图书表t_book中的评论量comment字段。
insert_sql = "insert into t_comment(`id`,`comment_name`,`comment_content`,`comment_time`) " \
             "values(1,'Tom','白嫖，还不错','2020-06-06');"
cursor.execute(insert_sql)
update_sql = "update t_book set `comment`=`comment`+1 where `id`=1;"
cursor.execute(update_sql)
#关闭游标
cursor.close()
#关闭链接
conn.close()

