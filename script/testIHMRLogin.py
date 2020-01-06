import logging
import sys
import unittest
from parameterized import parameterized
from api.loginApi import LoginApi
from app import HEADERS
from readData.read_json import build_login_data
from utils import assert_commen


class TestIHMRLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    @parameterized.expand(build_login_data())
    def test_login(self, mobile, password, status_code, success, code, message):
        """登录接口测试"""

        print(mobile, password, status_code, success, code, message)
        resp = self.login_api.login_resp(mobile, password)
        jsonData = resp.json()
        logging.info('登录成功接口返回的数据为：{}'.format(jsonData))
        try:
            # 断言
            assert_commen(self, resp, status_code, success, code, message)
        except AssertionError as e:
            logging.info(sys.exc_info()[1])
            raise e

