'''
fixture 可带参数与返回值
'''
# 测试前置:准备测试数据,在测试用例中使用测试数据。测试数据用fixture的返回值来表示
import pytest


@pytest.fixture()
def uname_pwd():
    return {'uname': 'root', 'pwd': '123456'}


# def test_login01(uname_pwd):
#     print(f'测试数据为:{uname_pwd["uname"], int(uname_pwd["pwd"])}')


@pytest.fixture(params=['宇宙恶魔·萝什', {'卢本伟': {"伞兵一号": "盖亚"}}, '阿婆克列', '伊斯塔废灵'])
def data(request):
    return request.param


@pytest.fixture(params=[
    {'uname': '卢本伟', 'pwd': '牛逼'},
    {'uname': '乔碧萝', 'pwd': '榜一'}])
def data1(request):
    return request.param


def test_login02(data):
    if type(data) == dict:
        print(f'\n\t用户{data["卢本伟"]["伞兵一号"]}登录')
    else:
        print(f'\n\t用户{data}登录')


def test_login03(data1):
    print(f"\n\t{data1['uname']}{data1['pwd']}")
