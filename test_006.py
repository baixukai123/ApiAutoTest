'''
1、接口测试场景较难模拟，需要大量工作才能完成
2、依赖第三方接口，但是第三方接口没有开发完成
    测试环境不充分情况下，如何测试？使用mock来模拟
'''
import mock

import requests


class Alipay:
    def zhifu(data):
        # 接口功能尚未完成
        # 接口地址、get/post、入参、返回值已定义好，有对应的接口文档
        # 接口参数:"OrderId":"12345678","Amount":128.5,"Type":"支付宝"
        # 接口返回值:"code": 200, "msg": "支付成功"
        r = requests.post("http://zhifubao.com/pay", data=data).json()
        return r


class TestMock:
    def test_alipay(self):
        # 对要模拟的类创建对象
        aliPay = Alipay()
        # 模拟zhifu的返回值为{"code": 200, "msg": "支付成功"},接口实现后可注释掉
        aliPay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
        # 调用zhifu接口
        data = {"OrderId": "12345678", "Amount": 128.5, "Type": "支付宝"}
        r = aliPay.zhifu(data)
        print(r)
