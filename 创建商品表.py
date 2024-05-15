from mysql_util import MysqlUtil

db = MysqlUtil()
#导航表
sql = """
CREATE TABLE `user1` (
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `repassword` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

category = db.insert(sql)  # 获取多条记录

# db = MysqlUtil()
# #导航表
# sql = """
# CREATE TABLE `category_temp` (
#   `id` varchar(50) NOT NULL,
#   `cname` varchar(255) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# """
#
# category = db.insert(sql)  # 获取多条记录

#商品表



# print("ok")