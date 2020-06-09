import unittest

import requests

session = requests.Session()
verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
session.get(verify_url)

login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
data = {"username": "13456789012", "password": "123456", "verify_code": "8888"}
response_login = session.post(url=login_url,data=data)
print('打印登陆结果：', response_login.json())
session.close()

class Fengzhuang(unittest.TestCase):
    def __init__(self):
        super().__init__()
        verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    @classmethod
    def setUpClass(cls):
        cls.session=requests.session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def get_verify(self):
        return session.get(verify_url)

    def test01_login_success(self):
        