"""
登录接口
"""
import requests
import app


# 登录接口：返回登录接口的响应对象，常用常量放到app模块中
class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + '/api/sys/login'
        self.headers = app.HEADERS

    def login_resp(self, mobile, pwd):
        data = {
            'mobile': mobile,
            'password': pwd
        }
        return requests.post(self.login_url, json=data, headers=self.headers)





































