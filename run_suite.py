import unittest

from script.testEmpApi import TestEmpApi
from script.testIHMRLogin import TestIHMRLogin

suite = unittest.TestSuite()

# 先添加先执行

# 登录模块
suite.addTest(unittest.makeSuite(TestIHMRLogin))

# 员工模块-增查改删
suite.addTest(unittest.makeSuite(TestEmpApi))

unittest.TextTestRunner().run(suite)
# report_path = BASE_DIR + '/report/ihrm{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))
# with open(report_path, 'wb') as f:
#     runner = HTMLTestRunner(f, verbosity=1, title='IHRM人力资源接口测试', description='v1.0.0')
#     runner.run(suite)
