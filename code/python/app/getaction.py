#! usr/bin/python3
# -*- coding: utf-8 -*-


from flask import jsonify


#连接数据库
def con():
    db_host = '119.23.36.18'
    db_user = 'test_market'
    db_passed = 'GrZFWfSh4GTMRBFy'
    return mysql.connector.connect(host = db_host, user = db_user, passwd = db_passed)


def check(a, b):
    if a == b:
        return True


def login(user, password):
    return 'hi ' + user


def regist(user, password, heading,nickname):
    r = {
        'value' : 0
    }
    mydb = con()
    if mydb == None:
        r['value'] = - 1
    else:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO user_db VALUES( ," + wxid + "," + heading + "," + int(time.time()) + ", '')")
        r['value'] = 1
    return r


def getUserInfo(token):
	pass
