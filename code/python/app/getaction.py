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
        # print(myresult)
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
        'value': 0,
        'token': ''
    }
    # 1： 正常、 -1：密码错误、 -2：封号、 -101：数据库连接失败、 -102：更新token异常、 -103：更新token失败（未注册）
    if checkPSW(user, password):
        return dueR(r, -1)
    # mydb = con()
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
        'value': 0
    }
    # 1： 正常、 -1：密码错误、 -101：数据库连接失败、 -102：插入异常（重复注册）、 -103：插入失败
    if checkPSW(user,password):
        return dueR(r, -1)
    # mydb = con()
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
    try:
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
    except:
       return dueR(r, -102)

def rollBackOrder(mydb, token, rollBackOrder):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 -2：订单id不存在 -101：数据库连接失败、 -102：sql异常
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    try:
        mycursor = mydb.cursor()
        mycursor.execute(
            "UPDATE order_db SET order_type=3  WHERE wxid=%s AND id=%s", (user, rollBackOrder))
        mydb.commit()
        if mycursor.rowcount == 0:
            return dueR(r, -2)
        return dueR(r, 1)
    except:
       return dueR(r, -102)
    return dueR(r, -666)

def getUserInfo(mydb, token):
    r = {
        'value': 0,
        'wxid': ''
    }
    # 1： 正常、 -1：token错误
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1
    return jsonify(r)


def joinMatch(mydb, token, matchid):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在

    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # get wxid according token
        sql = "SELECT wxid FROM user_db WHERE token = %s"
        val = (token,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        wxid = myresult[0]

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        # check wxid - match_id unique
        sql = "SELECT * FROM competitor_db WHERE match_id = %s AND wxid = %s"
        val = (matchid, wxid)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult != None:
            return dueR(r, -3)

        # get init_money from match_db
        sql = "SELECT init_money FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        init_money = myresult[0]

        # add into competitor_db
        sql = "INSERT INTO competitor_db (match_id, wxid, balance) VALUES (%s, %s, %s)"
        val = (matchid, wxid, init_money)
        mycursor.execute(sql, val)
        mydb.commit()

        # # add into storage_db
        # sql = "INSERT INTO storage_db (wxid, match_id, stock_id, own_num, ave_price, lock_num) VALUES (%s, %d, %s, %d, %f, %d)"
        # val = (wxid, matchid, "", 0, 0.0, 0)
        # mycursor.execute(sql, val)
        # mydb.commit()

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def quitMatch(mydb, token, matchid):
    r = {
        'value': 0,
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛

    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # get wxid according token
        sql = "SELECT wxid FROM user_db WHERE token = %s"
        val = (token,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        wxid = myresult[0]

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        # delete from competitor_db
        sql = "SELECT * FROM competitor_db WHERE match_id = %s AND wxid = %s"
        val = (matchid, wxid)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -5)

        sql = "DELETE FROM competitor_db WHERE match_id = %s AND wxid = %s"
        val = (matchid, wxid)
        mycursor.execute(sql, val)
        mydb.commit()

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def getMatchInfo(mydb, token, matchid):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛

    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        r['id'] = myresult[0]
        r['match_name'] = myresult[1]
        r['match_detail'] = myresult[2]
        r['match_rule'] = myresult[3]
        r['start_time'] = myresult[4]
        r['sign_time'] = myresult[5]
        r['end_time'] = myresult[6]
        r['init_money'] = myresult[7]

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def getMatchList(mydb, token):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛

    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # check match
        sql = "SELECT * FROM match_db"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult == []:
            return dueR(r, -4)

        matchlist = []
        for x in myresult:
            tmp = {'id': x[0], 'match_name': x[1]}
            matchlist.append(tmp)

        r['matchlist'] = matchlist

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def getMatchRank(mydb, token, matchid):
    r = {
        'value': 0,
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛  -6: 暂无参赛人员

    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        # competitor_db sorted by balance
        sql = "SELECT * FROM competitor_db WHERE match_id = %s ORDER BY balance DESC LIMIT 10"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if myresult == []:
            return dueR(r, -6)

        ranklist = []
        for x in myresult:
            tmp = {'wxid': x[2], 'balance': x[3]}
            ranklist.append(tmp)

        r['ranklist'] = ranklist

        return dueR(r, 1)
    except:
        return dueR(r, -102)
