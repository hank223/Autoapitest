import requests
response = requests.get("http://www.baidu.com/s?wd=xxx")
print('搜索结果是：',response.text)