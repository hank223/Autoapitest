import requests
session = requests.Session()
verify_url = "http://localhost/index.php?m=HOme&c=User&a=verify"
session.get(url=verify_url)
login_url ="http://localhost/index.php?m=Home&c=User&a=do_login"
data = {"username":"13456789012","password":"123456","verify_code":"8888"}
response_login =session.post(url=login_url,data=data)
print('登陆结果为：',response_login.json())

response_order =session.get(url="http://localhost/Home/Order/order_list.html")
print('我的订单页面：',response_order.text)