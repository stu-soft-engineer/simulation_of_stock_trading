#! usr/bin/python3
# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from flask import request

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
        user = request.form['user']
        psw = request.form['psw']
        r = getaction.login(user, psw)
        return r
    elif ac == 'signup':
        user = request.form['user']
        psw = request.form['psw']
        r = getaction.regist(user, psw)
        return r
    return '<h3>Bad request.</h3>'
