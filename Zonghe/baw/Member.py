'''
用户模块接口（注册、登录、充值、获取用户列表、取现...）
'''


def register(url, baserequests, data):
    '''
    发送注册接口
    :param url: http://jy001:8081/
    :param baserequests: 是Baserequests的一个实例
    :param data: 注册接口的参数
    :return: 响应信息
    '''

    url += "futureloan/mvc/api/member/register"
    baserequests_post = baserequests.post(url, data=data)
    return baserequests_post


def login(url, baserequests, data):
    '''
    发送注册接口
    :param url: http://jy001:8081/
    :param baserequests: 是Baserequests的一个实例
    :param data: 登录接口的参数
    :return: 响应信息
    '''

    url += "futureloan/mvc/api/member/login"
    baserequests_post = baserequests.post(url, data=data)
    return baserequests_post


if __name__ == '__main__':
    from Zonghe.caw.BaseRequests import BaseRequests
    # # 测试注册代码
    # base_register = BaseRequests()
    # canshu = {"mobilephone": 18112341234, "pwd": 123456}
    # r = register("http://jy001:8081/", base_register, canshu)
    # print(r.json())

    # # 测试登录代码
    # base_login = BaseRequests()
    # canshu = {"mobilephone": 18112341234, "pwd": 123456}
    # r = login("http://jy001:8081/", base_login, canshu)
    # print(r.json())
