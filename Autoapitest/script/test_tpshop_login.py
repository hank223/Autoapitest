import unittest
import requests
from parameterized import parameterized

from Autoapitest import app
from Autoapitest.api.tpshop_enroll_api import EnrollTpshop
from Autoapitest.api.tpshop_login_api import TestTpshopApi
from Autoapitest.app import read_data, assert_enroll, assert_login


class TpshopLogin(unittest.TestCase):
    filepath = app.BASE_DIR + "/data/data.json"

    @classmethod
    def setUp(self):
        self.session = requests.Session()
        self.login_api = TestTpshopApi()
        self.login_enroll_api = EnrollTpshop()

    @classmethod
    def tearDown(self):
        if self.session != None:
            self.session.close()

    # def test01_login_success(self):
    #     response = self.login_api.get_verify(self.session)
    #     data = {"username":"13456789012","password":"123456","verify_code":"8888"}
    #     response = self.login_api.login(self.session,data)
    #     print(response.json())
    #     self.assertEqual(200,response.status_code)

    @parameterized.expand(read_data(filepath))
    def test01_login_enroll(self, enroll_data, status, msg1, login_data, msg2, status_code):
        # 通过session访问注册验证码获取cookie
        self.login_enroll_api.get_enroll_verify(self.session)
        # 注册
        response_enroll = self.login_enroll_api.enroll(self.session, enroll_data)
        # 断言注册
        assert_enroll(self, status, msg1, response_enroll)
        # 通过session访问登陆验证码获取cookie
        self.login_enroll_api.get_login_verify(self.session)
        # 登陆
        response_login = self.login_enroll_api.login_enroll(self.session, login_data)
        # 断言登陆
        assert_login(self, msg2, status_code, response_login)
