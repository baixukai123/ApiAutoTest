'''
灵活测试前后置，fixture
不受setup,teardown命名限制
使用灵活
'''

import pytest


# 测试前置,使用fixture修饰
@pytest.fixture(scope='module')  # scope默认function级别,module级:首次调用执行前置，全部用例执行完，执行后置
def login():
    print("登入")  # yield 前是前置
    yield
    print("登出")  # yield 后是后置


@pytest.fixture(autouse=True)
def db_op():
    print("连接数据库")
    yield
    print("断开数据库连接")


def test_01():
    print("1、查询不用登陆")


def test_02(login):
    print("2、添加需要登录")


@pytest.mark.usefixtures('login')
def test_03():
    print("3、删除需要登录")
