# 导入requests模块
import requests
# 初始化session对象
session = requests.Session()
# 先使用session实例调用注册的获取验证码接口
response = session.get("http://localhost/index.php/Home/User/verify/type/user_reg.html")
# 然后使用session实例调用注册接口
reg_data = "auth_code=TPSHOP&scene=1&username=13145201413&verify_code=8888&password=5194752 28fe35ad067744465c42a19b2&password2=519475228fe35ad067744465c42a19b2"
response2 = session.post("http://localhost/index.php/Home/User/reg.html", data=reg_data,headers={"Content-Type": "application/x-www-form-urlencoded"})
# 输出注册结果
print("Result: ", response2.json())