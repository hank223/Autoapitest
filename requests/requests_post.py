import requests
response = requests.post(url='http://localhost/index.php?m=Home&c=User&a=do_login',data={'username':'13800138006','password':'123456','verify_code':'8888'})
print('tpshop的登陆结果为：',response.text)