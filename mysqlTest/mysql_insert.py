#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector

# 打开数据库连接
db = mysql.connector.connect(user='root',passwd='lds1992',database='test')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
sql = '''INSERT INTO EMPLOYEE(FIRST_NAME,
       LAST_NAME, AGE, SEX, INCOME) 
       VALUES ('%s', '%s', '%s', '%s', '%s' )''' % \
      ('Mac', 'Mohan', 40, 'M', 6012.34)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()

except:
    # Rollback in case there is any error
    db.rollback()

# 关闭数据库连接
db.close()