# # import time
# # for i in range(100):
# #     time.sleep(0.2)
# #     print(f'\r\033[3{i%10};4{i%10}mThis is a test !\033[0m',end='',flush=True)
# #     # print(f'\033[32mThis is a test !\033[0m', end='',flush=True)
# #
# #
#
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Datatime:2022/7/31 20:21
# # Filename:017 Python 流程控制之 if 判断.py
# # Toolby: PyCharm
# # 坚持
#
# # 变量
# # 数据类型
# # 输入输出
# # 基本运算符
#
#
# # if
# '''
# if 条件成立:
#     可以干一些事情
# '''
# # name = input("请问冲过来的是什么（dog, girl)：")
# # if name == 'girl':
# #     print("亲爱的，我来了")
# #
# #
# # print('滚一边去，狗')
#
# '''
# if 条件成立：
#     走这里
# elif 条件成立：
#     走这里
# elif ……可以有很多个
# '''
#
#
# # name = input("请问冲过来的是什么（dog, girl,boy)：")
# # if name == 'girl':
# #     print("亲爱的，我来了")
# # elif name == 'dog':
# #     print("疯狗，走开")
# # elif name == 'boy':
# #     print("抱歉，不搞基")
# #
# #
# # print('傻 x，让你输入 dog、girl、boy')
#
# '''
# if 条件1成立：
#     1走这里
# elif 条件 2 成立：
#     2走这里
# elif 条件 3 成立：
#     3 走这里
# else：
#     如果上述都不成立，走这里
# '''
#
#
# # name = input("请问冲过来的是什么（dog, girl,boy)：")
# # if name == 'girl':
# #     print("亲爱的，我来了")
# # elif name == 'dog':
# #     print("疯狗，走开")
# # elif name == 'boy':
# #     print("抱歉，不搞基")
# # else:
# #     print('傻 x，让你输入 dog、girl、boy')
#
#
# name = input("请问冲过来的是什么（dog, girl,boy)：")
# if name == 'girl':
#     print("亲爱的，我来了")
#
# if name == 'dog':
#     print("疯狗，走开")
#
# if name == 'boy':
#     print("抱歉，不搞基")
#
#
# '''
# https://www.cnblogs.com/nickchen121/p/10737326.html
# 3.1 练习1：成绩评判
# 如果 成绩>=90，打印"优秀"
# 如果 成绩>=80 并且 成绩<90，打印"良好"
# 如果 成绩>=70 并且 成绩<80，打印"普通"
# 其他情况：打印"差"
# '''
#
#
import base64
import datetime
import hashlib
import os
import string
from random import random

import requests
from flask import Flask, render_template, request, json, jsonify, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


# 首页
@app.route('/')
def index():
    # # return 'Hello, World'
    # return render_template('./index.html')

    # 如果未登录，就跳转到 login
    if 'userinfo' not in session:
        return redirect('/login')

    # 已登录，渲染模板
    return render_template("./index.html")


# 登录
# @app.route('/login')
# def login():
#     # return '登录成功'
#     return render_template('./login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 渲染 login.html 模板文件并返回
        return render_template('login.html')

    # 处理 POST 请求
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # 读取 userlist.json 文件
    try:
        with open('./data/userlist.json', 'r') as f:
            userlist = json.load(f)
    except FileNotFoundError:
        return jsonify({'code': 0, 'message': '账号或者密码错误'})

    # 判断 username 是否为 userlist 对象的属性
    if username not in userlist:
        return jsonify({'code': 0, 'message': '账号或者密码错误'})

    # 对密码进行校验
    password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    if password_md5 != userlist[username]['password']:
        return jsonify({'code': 0, 'message': '账号或者密码错误'})

    # 将用户信息写入 session
    session['userinfo'] = username

    return jsonify({'code': 1, 'message': '登录成功'})


# 注册
# @app.route('/register')
# def register():
#     # return '注册成功'
#     return render_template('./register.html')
# 图片列表
# @app.route('/imglist')
# def img_list():
#     # # return '图片列表'
#     # return render_template('./imglist.html')
#     # 如果未登录，就跳转到 login
#     if 'userinfo' not in session:
#         return redirect('/login')
#
#     # 已登录，渲染模板
#     return render_template('./imglist.html')
#

# 图片列表
@app.route('/imglist')
def imglist():
    # 如果未登录，就跳转到 login
    if 'userinfo' not in session:
        return redirect('/login')

    username = session['userinfo']

    img_file_path = './data/imglist.json'

    try:
        with open(img_file_path, 'r') as f:
            img_dict = json.load(f)

        user_img_list = []
        if img_dict and username in img_dict:
            user_img_list = img_dict[username]

    except Exception as e:
        user_img_list = []

    return render_template('imglist.html', user_img_list=user_img_list)


# @app.route('/api/data')
# def get_data():
#     # 处理请求并返回响应数据
#     data = {'name': 'John', 'age': 25}
#     return jsonify(data)


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # 渲染 register.html 模板文件并返回
        return render_template('register.html')
    else:

        data = request.get_json()
        print(data)
        username = data.get('username')
        password = data.get('password')

        try:
            with open('./data/userlist.json', 'r') as f:
                userlist = json.load(f)
        except FileNotFoundError:
            userlist = {}

        if username in userlist:
            return jsonify({'code': 0, 'message': '注册失败，用户名已经被使用了'})

        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        date = datetime.date.today().strftime('%Y-%m-%d')

        userlist[username] = {'username': username, 'password': password, 'register_date': date}

        with open('./data/userlist.json', 'w+') as f:
            json.dump(userlist, f, indent=4)

        return jsonify({'code': 1, 'message': '恭喜您注册成功'})


# 退出
@app.route('/logout')
def logout():
    session.pop('userinfo', None)
    return redirect('/login')


# 文生图的路由
# @app.route('/generateimg', methods=['POST'])
# def generate_img():
#     data = request.get_json()
#     print(data)
#     return jsonify({'code': 1, 'message': '图片生成成功'})

# 文生图的路由
@app.route('/generateimg', methods=['POST'])
def generate_img():
    data = request.get_json()
    url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'

    # 向指定 URL 发送 POST 请求
    try:
        response = requests.post(url, json=data, timeout=30)
    except requests.exceptions.Timeout:
        return jsonify({'code': 0, 'message': '图片生成失败，超时'})

    # 处理响应数据
    result = response.json()

    # 创建保存图片的目录
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    save_dir = os.path.join(os.getcwd(), 'static', today)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 保存图片并记录路径
    img_paths = []

    for i, img_base64 in enumerate(result['images']):
        # 生成随机文件名
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + '.png'
        # 保存文件
        save_path = os.path.join(save_dir, filename)
        with open(save_path, 'wb') as f:
            f.write(base64.b64decode(img_base64))
        # 记录路径
        img_paths.append(os.path.join('static', today, filename).replace('\\', '/'))
        # 添加图片信息到 user_img_list
        user_img_list = []

        img_info = {'path': os.path.join('static', today, filename).replace('\\', '/'), 'date': today}
        user_img_list.append(img_info)

    # 返回 JSON 数据
    return jsonify({'code': 1, 'message': '图片生成成功', 'img_paths': img_paths})


def save_img_list(user_img_list):
    # user_img_list = [{'path': 'static/2023-06-26/4', 'date': '2023-06-26'}, {'path': 'static/2023-06-26/2', 'date': '2023-06-26'}, {'path': '3', 'date': '2023-06-26'}]

    # 判断文件是否存在，如果不存在就创建一个空的文件
    if not os.path.exists('./data/imglist.json'):
        with open('./data/imglist.json', 'w') as f:
            json.dump({}, f)

    # 读取 imglist.json 文件中的内容
    with open('./data/imglist.json', 'r') as f:
        imglist = json.load(f)

    # 获取当前登录用户的用户名
    # username = session.get('userinfo', {}).get('username')
    username = 'user_002'

    # 如果 imglist 中已经存在该用户的数据，就将新的图片列表合并到该用户的数据中
    if username in imglist:
        imglist[username] = user_img_list + imglist[username]
    # 如果 imglist 中不存在该用户的数据，就直接将新的图片列表作为该用户的数据
    else:
        imglist[username] = user_img_list

    # 将更新后的 imglist 写入 imglist.json 文件中
    with open('./data/imglist.json', 'w') as f:
        json.dump(imglist, f, indent=4)

    return 'test func'


if __name__ == '__main__':
    app.run(port=9526, debug=True)
