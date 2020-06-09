import requests


class EnrollTpshop:
    def __init__(self):
        self.enroll_verify = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
        self.enrll_url = "http://localhost/index.php/Home/User/reg.html"
        self.login_verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_enrollurl = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def get_enroll_verify(self, session):
        return session.get(self.enroll_verify)

    def enroll(self, session, enroll_data):
        return session.post(url=self.enrll_url, headers=self.headers, data=enroll_data)

    def get_login_verify(self, session):
        return session.get(self.login_verify_url)

    def login_enroll(self, session, login_data):
        return session.post(url=self.login_enrollurl, headers=self.headers, data=login_data)
