import unittest

from app import BASE_DIR
from script.testEmpApi import TestEmpApi
from script.testIHMRLogin import TestIHMRLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

# 先添加先执行

# 登录模块
# suite.addTest(unittest.makeSuite(TestIHMRLogin))

# 员工模块-增查改删
suite.addTest(unittest.makeSuite(TestEmpApi))

# unittest.TextTestRunner().run(suite)
report_path = BASE_DIR + '/report/ihrm.html'
with open(report_path, 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=1, title='IHRM人力资源接口测试', description='v1.0.0')
    runner.run(suite)
