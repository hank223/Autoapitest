import requests
class TestTpshopApi:
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
    def get_verify(self,session):
        return session.get(self.verify_url)

    def login(self,session,data):
        return session.post(url=self.login_url,data=data)