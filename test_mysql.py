from mysql_util import MysqlUtil


db = MysqlUtil()

sql = 'SELECT * FROM product'
product_list = db.fetchall(sql)  # 获取多条记录

print(product_list)

