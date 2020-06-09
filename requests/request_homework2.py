#导包
import requests
#实例化Session
session = requests.Session()
#验证码url
verify_url = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
#注册url
enroll_url = "http://localhost/index.php/Home/User/reg.html"
#通过访问验证码，将cookie保存入session
session.get(verify_url)
#注册请求参数
data = "auth_code=TPSHOP&scene=1&username=13145201413&verify_code=8888&password=519475228fe35ad067744465c42a19b2&password2=519475228fe35ad067744465c42a19b2"
response = session.post(url=enroll_url,data=data,headers={"Content-Type": "application/x-www-form-urlencoded"})
print(response.json())