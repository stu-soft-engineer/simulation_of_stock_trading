#! usr/bin/python3
# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from flask import request
from app import getaction
from app import ssql

mydbcon = ssql.SQLink()
print('林肯死大头！', mydbcon)

@app.route('/')
@app.route('/index')
def action_index():
    user = {'username': 'visitor'}
    posts = [
        {
            'author': {'username': 'You'},
            'body': 'This page was built on 2018/12/10!'
        },
        {
            'author': {'username': 'Yang'},
            'body': 'What\'s more? 17:00'
        }
    ]
    return render_template('index.html', title='STU', user=user, posts=posts)


@app.route('/<ac>', methods=['POST'])
def to_do(ac):
    global mydbcon
    mydb = mydbcon.get_db() # 这个是数据库连接

    if ac == 'login':
        # 登录
        try:
            user = request.form['user']  # wxid
            psw = request.form['psw']   # 密码
        except:
            pass
        else:
            r = getaction.login(mydb, user, psw)
            return r
               
    elif ac == 'regist':
        # 注册
        try:
            user = request.form['user'] # weid
            psw = request.form['psw']   # 密码
            heading = request.form['heading']     # 头像
            nickName = request.form['nickname']   # 昵称
        except:
            pass
        else:
            r = getaction.regist(mydb, user, psw, heading, nickName)
            return r
    
    elif ac == 'getUserInfo':
        #获取用户个人信息（我的比赛、持仓信息）
        try:
            token = request.form['token']# token
        except:
            pass
        else:
            r = getaction.getUserInfo(mydb, token)
            return r

    elif ac == 'buy':
        #买入股票
        try:
            token = request.form['token']  # token
            matchID = request.form['matchid']  # 比赛的id
            stockID = request.form['stockid']  # 股票id
            stockNumber = request.form['stocknum']  # 股票数量
            stockPrice = request.form['price']  # 买入价格
        except:
            pass
        else:
            r = getaction.buyOrder(mydb, token, matchID=matchID, stockID=stockID, buyNum=stockNumber, stockPrice=stockPrice)
            return r

    elif ac == 'sell':
        #卖出股票
        try:
            token = request.form['token']  # token
            matchID = request.form['matchid']  # 比赛的id
            stockID = request.form['stockid']  # 股票id
            stockNumber = request.form['stocknum']  # 股票数量
            stockPrice = request.form['price']  # 卖出价格
        except:
            pass
        else:
            r = getaction.sellOrder(mydb, token, matchID=matchID, stockID=stockID, sellNum=stockNumber, stockPrice=stockPrice)
            return r

    """ 
    elif ac == 'joinMatch':
        #报名比赛（）
        token = request.form['token']# token
        matchID = request.form['matchid']# 比赛的id
        return r

    elif ac == 'quitMatch':
        #退出比赛（）
        token = request.form['token']# token
        matchID = request.form['matchid']# 比赛的id
        return r

    elif ac == 'getMatchInfo':
        #获取比赛信息
        token = request.form['token']# token
        matchID = request.form['matchid']# 比赛的id
        return r

    elif ac == 'getMatchRank':
        #获取比赛前十名
        token = request.form['token']# token
        matchID = request.form['matchid']# 比赛的id
        return r

    elif ac == 'getStockInfo':
        #获取股票信息
        token = request.form['token']# token
        stockID = request.form['stockid']# 股票的id
        return r

    elif ac == 'rollBackOrder':
        #撤销订单
        token = request.form['token']# token
        orderID = request.form['orderid']# 订单的id
        return r

    elif ac == 'getUserOrder':
        #查询该用户的所有状态的订单
        token = request.form['token']# token
        return r 
    
    """

    return '<h3>Bad request.</h3>'


