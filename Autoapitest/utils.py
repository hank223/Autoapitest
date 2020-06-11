import os
import time
import unittest

# 创建测试套件
import HTMLTestRunner_PY3

from Autoapitest import app
from Autoapitest.script.test_tpshop_login import TpshopLogin
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
suite = unittest.TestSuite()
# 将测试用例添加到测试组件
suite.addTest(unittest.makeSuite(TpshopLogin))
# 定义测试报告的目录和名称
report_path = BASE_DIR + "/report/tpshop_login.html"
with open(report_path, mode='wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title='tpshop登陆接口功能测试', description='需要联网')
    runner.run(suite)