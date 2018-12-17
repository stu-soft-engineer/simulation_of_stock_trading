#! usr/bin/python3
# -*- coding: utf-8 -*-
from flask import jsonify
import time
import hashlib
import mysql.connector
from app import stock
from app import competitor

def dueR(r, v):  # 将字典r的value项改成v的值，并且转成json
    r['value'] = v
    return jsonify(r)


def checkPSW(a, b):  # in：用户名，密码 out：真假 for：检测出密码不正确返回真
    if a == b:
        return False
    else:
        return True


def checkTOKEN(token, mydb):  # in：token,mydb out：wxid for：检测出token的用户id
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT wxid FROM user_db WHERE token = %s", (token,))
        myresult = mycursor.fetchone()
        #print(myresult)
    except:
        return None
    else:
        if myresult != None:
            return myresult[0]
    return None
            

def getTimeStamp():  # 获取10位整数时间戳
    return int(time.time())


def getToken(user):  # 加密获取token
    md5 = hashlib.md5()
    token = user + '-' + str(getTimeStamp())
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()


def login(mydb, user, password):
    r = {
        'value' : 0,
        'token' : ''
    }
    # 1： 正常、 -1：密码错误、 -2：封号、 -101：数据库连接失败、 -102：更新token异常、 -103：更新token失败（未注册）
    if checkPSW(user,password):
        return dueR(r, -1) 
    #mydb = con()
    if mydb == None:
        return dueR(r, -101) 
    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT count(*) FROM blacklist_db WHERE wxid = %s", (user,))
        myresult = mycursor.fetchone()
        print(myresult)
    except:
        return dueR(r, -102)
    else:
        if myresult[0] > 0:
            return dueR(r, -2)

    token = getToken(user)
    try:
        mycursor.execute("UPDATE user_db SET token=%s WHERE wxid=%s", (token, user))
        mydb.commit()
    except:
        r['value'] = -102
    else:
        if mycursor.rowcount > 0:
            r['value'] = 1
            r['token'] = token
        else:
            r['value'] = -103
    return jsonify(r) 


def regist(mydb, user, password, heading, nick):
    r = {
        'value' : 0
    }
    # 1： 正常、 -1：密码错误、 -101：数据库连接失败、 -102：插入异常（重复注册）、 -103：插入失败
    if checkPSW(user,password):
        return dueR(r, -1) 
    #mydb = con()
    if mydb == None:
        return dueR(r, -101) 
    try:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO user_db (wxid, heading, regist_time, nickName) VALUES (%s, %s, %s, %s)", (user, heading, getTimeStamp(), nick))
        mydb.commit()
    except:
        r['value'] = -102
    else:
        if mycursor.rowcount > 0:
            r['value'] = 1
        else:
            r['value'] = -103
    return jsonify(r) 



def buyOrder(mydb, token, *, matchID, stockID, buyNum, stockPrice):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    try:
        buyNum = int(buyNum)
        balance = competitor.getBalance(mydb, matchID, user)  # 查询余额
        price = int(buyNum) * float(stockPrice) # 需要多少钱
        if balance < price:
            return dueR(r, -2)
        balance -= price
        if competitor.updateBalance(mydb, matchID, user, balance) == False:  # 更新余额
            return dueR(r, -103)
        # 加入订单
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO order_db (order_type, wxid, creat_time, order_status, stock_id, order_num, price) VALUES ( %s, %s, %s, %s, %s, %s, %s)",
            (1, user, getTimeStamp(), 1, stockID, buyNum, stockPrice))
        mydb.commit()
        if mycursor.rowcount == 0:
            return dueR(r, -103)
        return dueR(r, 1)
    except:
        return dueR(r, -102)
    return dueR(r, -666)


def sellOrder(mydb, token, *, matchID, stockID, sellNum, stockPrice):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 -2：库存不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    #try:
    ownNum = competitor.getStockNum(mydb, matchID, user, stockID)  # 查询余额
    sellNum = int(sellNum)
    if ownNum < sellNum:
        return dueR(r, -2)
    ownNum -= sellNum
    if competitor.updateStockNum(mydb, matchID, user, stockID, ownNum) == False:  # 更新余额
        return dueR(r, -103)
    # 加入订单
    mycursor = mydb.cursor()
    mycursor.execute(
        "INSERT INTO order_db (order_type, wxid, creat_time, order_status, stock_id, order_num, price) VALUES ( %s, %s, %s, %s, %s, %s, %s)",
        (2, user, getTimeStamp(), 1, stockID, sellNum, stockPrice))
    mydb.commit()
    if mycursor.rowcount == 0:
        return dueR(r, -103)
    return dueR(r, 1)
    #except:
    #   return dueR(r, -102)


def getUserInfo(mydb, token):
    r = {
        'value': 0,
        'wxid': ''
    }
    # 1： 正常、 -1：token错误
    #mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1
    pass
    return jsonify(r)
