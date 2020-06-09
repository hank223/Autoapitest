# 导入os模块
import json
import os

# 定义全局变量BASE_DIR，通过BASE_DIR定位到项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 定义请求头
HEADERS = None
# 定义员工ID
EMP_ID = None


def assert_enroll(self, status, msg1, response_enroll):
    self.assertEqual(status, response_enroll.json().get('status'))
    self.assertIn(msg1, response_enroll.json().get('msg'))


def assert_login(self, msg2, status_code, response_login):
    self.assertIn(msg2, response_login.json().get('msg'))
    self.assertEqual(status_code, response_login.status_code)


def read_data(filepath):
    # 编写读取登录数据的函数
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for login_data in jsonData:  # type:dict
            # 把每一组登录数据的所有values转化为元组形式，并添加到空列表当中
            result_list.append(tuple(login_data.values()))

    print("查看读取的登录数据为：", result_list)
    return result_list
