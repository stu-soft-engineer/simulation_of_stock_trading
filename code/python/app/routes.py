#! usr/bin/python3
# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from flask import request
from app import getaction
@app.route('/')
@app.route('/index')
def action_index():
    user = {'username': 'Young'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'This page was built on 2018/12/10!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'What\'s more? 17:00'
        }
    ]
    return render_template('index.html', title='STU', user=user, posts=posts)


@app.route('/<ac>', methods=['POST'])
def to_do(ac):
    if ac == 'login':
        # 登录
        user = request.form['user'] # wxid
        psw = request.form['psw']   # 密码
        r = getaction.login(user, psw)
        return r
    elif ac == 'signup':
        # 注册
        user = request.form['user'] #weid
        psw = request.form['psw']   # 密码
        heading=request.form['heading']#头像
        nickName=request.form['nickname']#昵称
        r = getaction.regist(user, psw,)
        return r
    elif ac == 'getUserInfo':
        #获取用户个人信息（我的比赛、持仓信息）
        token = request.form['token']# token
      
        return r
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

    elif ac == 'buy':
        #买入股票
        token = request.form['token']# token
        matchID = request.form['matchid']# 比赛的id
        stockID=request.form['stockid']#股票id
        stockNumber=request.form['stocknum']#股票数量
        return r

    elif ac == 'sell':
        #卖出股票
        token = request.form['token']# token
        matchID = request.form['matchid']# 比赛的id
        stockID=request.form['stockid']#股票id
        stockNumber=request.form['stocknum']#股票数量
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



    return '<h3>Bad request.</h3>'


