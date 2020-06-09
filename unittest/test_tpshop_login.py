import unittest
import requests
class TestTpshopLogin(unittest.TestCase):
    def setUp(self):
        self.verify_url = "http://localhost/index.php?m=HOme&c=User&a=verify"
        self.login = "http://localhost/index.php?m=Home&c=User&a=do_login"
    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls):
        if cls.session !=None:
            cls.session.close()

    def test01_login_success(self):
        response_verify = self.session.get(url=self.verify_url)
        print('打印看一下，图片内容：',response_verify.content)
        print('打印验证码接口返回的响应头：',response_verify.headers)
        self.assertIn("image",response_verify.headers.get('Content-Type'))

        response_login =self.session.post(url=self.login,data={'username':'13456789012','password':'123456','verify_code':'8888'})
        print(response_login.json())
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(1,response_login.json().get('status'))
        self.assertIn('登陆成功',response_login.json().get('msg'))

    def test02_username_dose_not_exist(self):
        response_verify = self.session.get(url=self.verify_url)
        print('打印看一下，图片内容：', response_verify.content)
        print('打印验证码接口返回的响应头：', response_verify.headers)
        self.assertIn("image", response_verify.headers.get('Content-Type'))

        response_login = self.session.post(url=self.login, data={'username': '13333789012', 'password': '123456',
                                                                 'verify_code': '8888'})
        print(response_login.json())
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(-1, response_login.json().get('status'))
        self.assertIn('不存在', response_login.json().get('msg'))

    def test03_password_error(self):
        response_verify = self.session.get(url=self.verify_url)
        print('打印看一下，图片内容：', response_verify.content)
        print('打印验证码接口返回的响应头：', response_verify.headers)
        self.assertIn("image", response_verify.headers.get('Content-Type'))

        response_login = self.session.post(url=self.login, data={'username': '13456789012', 'password': '122226',
                                                                 'verify_code': '8888'})
        print(response_login.json())
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(-2, response_login.json().get('status'))
        self.assertIn('密码错误', response_login.json().get('msg'))
