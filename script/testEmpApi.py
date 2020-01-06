import logging
import sys
from unittest import TestCase

import pymysql
from parameterized import parameterized
import app
from api.empApi import EmpApi
from api.loginApi import LoginApi
from readData.read_json import build_insert_emp_data, build_query_del_emp_data, build_modify_emp_data
from utils import assert_commen, DBUtils


class TestEmpApi(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.emp_api = EmpApi()

    def test0_login(self):
        """登录接口测试"""
        resp = self.login_api.login_resp('13800000002', '123456')
        jsonData = resp.json()
        logging.info('登录成功接口返回的数据为：{}'.format(jsonData))
        try:
            # 断言
            assert_commen(self, resp, 200, True, 10000, '操作成功')
        except AssertionError as e:
            logging.info(sys.exc_info()[1])
            raise e

        # 令牌
        token = 'Bearer ' + resp.json().get('data')
        app.HEADERS['Authorization'] = token
        print('令牌:', token)

    @parameterized.expand(build_insert_emp_data)
    def test1_insert_emp_api(self, username, mobile, status_code, success, code, message):
        """新增员工"""
        resp = self.emp_api.add_emp(username, mobile)
        print(status_code, success, code, message)
        assert_commen(self, resp, status_code, success, code, message)
        jsonData = resp.json()
        logging.info('新增员工接口返回的数据为：{}'.format(jsonData))

        app.EMP_ID = jsonData.get('data').get('id')
        print('新增员工的id:', app.EMP_ID)

    @parameterized.expand(build_query_del_emp_data)
    def test2_query_emp_api(self, status_code, success, code, message):
        """查询员工"""
        resp = self.emp_api.query_emp()
        jsonData = resp.json()
        logging.info('查询员工接口返回的数据为：{}'.format(jsonData))

        assert_commen(self, resp, status_code, success, code, message)

    @parameterized.expand(build_modify_emp_data)
    def test3_update_emp_api(self, departmentName, status_code, success, code, message):
        """更新员工"""
        resp = self.emp_api.update_emp({"departmentName": departmentName})
        jsonData = resp.json()
        logging.info('更新员工接口返回的数据为：{}'.format(jsonData))

        sql = 'select * from bs_user where id={}'.format(app.EMP_ID)
        with DBUtils() as db_utils:
            db_utils.execute(sql)
            result = db_utils.fetchone()

        self.assertEqual(departmentName, result[-3])
        assert_commen(self, resp, status_code, success, code, message)

    @parameterized.expand(build_query_del_emp_data)
    def test4_del_emp_api(self, status_code, success, code, message):
        """删除员工"""
        resp = self.emp_api.del_emp()
        jsonData = resp.json()
        logging.info('删除员工接口返回的数据为：{}'.format(jsonData))

        assert_commen(self, resp, status_code, success, code, message)
