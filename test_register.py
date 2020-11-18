'''
pytest命名规则
'''

import requests


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


# 手机号格式不正确
def test_register_01():
    # 测试数据
    data = {"mobilephone": 18012304561, "pwd": 123456, "regname": "hello"}
    # 预期结果
    expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
