import requests
response = requests.get(url='http://www.baidu.com')
print('响应结果：',response.text)