"""工具类"""
import pymysql


def assert_commen(self, resp, status_code, success, code, message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, resp.json().get('success'))
    self.assertEqual(code, resp.json().get('code'))
    self.assertIn(message, resp.json().get('message'))


"""
❀——————    
    __enter__和__exit__是一对魔法方法，和with结合使用
        with open方法 as f:   文件处理，不用手动关闭文件
            ...
        with DBUtils() as cursor:   数据库处理，不用自己手动关闭游标和数据库连接
            ...
"""


class DBUtils(object):
    def __init__(self, host='182.92.81.159', user='readuser', pwd='iHRM_user_2019', db='ihrm'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.pwd, self.db)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
