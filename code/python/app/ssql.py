#! usr/bin/python3
# -*- coding: utf-8 -*-


class SQLink:
    db = None
    db_host = '119.23.36.18'
    db_user = 'test_market'
    db_passed = 'GrZFWfSh4GTMRBFy'

    """初始化，返回连接id"""
    def __init__(self):
        self.db = mysql.connector.connect(host=self.db_host, user=self.db_user, passwd=self.db_passed)

    """返回db对象"""
    def get_db(self):
        return self.db

    """关闭连接"""
    def turn_off(self):
        pass


""" 单个插入
mycursor = mydb.cursor()
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, mycursor.lastrowid， "记录插入成功。") """


""" 批量插入
mycursor = mydb.cursor()
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。") """


""" 查询数据
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
  print(x) """
