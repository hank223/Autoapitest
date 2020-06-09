import requests
response = requests.post(url='http://ihrm-test.itheima.net/api/sys/login',json={'mobile':'13800000002','password':'123456'})
print('打印的登陆结果是：',response.json())