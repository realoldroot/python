# -*- coding: utf-8 -*-
from flask import Flask, Response, jsonify, request


# 重写response返回json
class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False
app.response_class = MyResponse


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET'])
def login_from():
    return '''<form action="/login" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>'''


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        return {
            'username': username,
            'password': password
        }
    else:
        return '用户名或密码没有输入'


@app.errorhandler(404)
def not_found(error):
    print("404错误了,%s", error)
    result = {'error': '404'}
    return result


if __name__ == '__main__':
    app.run()
