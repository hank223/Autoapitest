import requests

session = requests.Session()
response1 = session.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
print(response1.json())
token = 'Bearer '+response1.json().get('data')
response2 = session.post(url="http://ihrm-test.itheima.net/api/sys/profile",
                         headers={"Content-Type": "application/json", "Authorization": token})

print(response2.url, response2.encoding, response2.cookies, response2.headers,
      response2.json(), response2.status_code,
      sep='\n')
