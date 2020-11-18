'''
fixture作用域:
默认function级别,有function，module，class，session级别
'''
import pytest


# 测试前置,使用fixture修饰
@pytest.fixture(scope='class')
def login():
    print("登入")  # yield 前是前置
    yield
    print("登出")  # yield 后是后置


class TestQuery():
    def test_case1(self):
        print('测试查询1')

    def test_case2(self, login):
        print('测试查询2')

    def test_case3(self):
        print('测试查询3')


class TestDelete():
    def test_case1(self, login):
        print('测试删除1')

    def test_case2(self, login):
        print('测试删除2')

    def test_case3(self):
        print('测试删除3')

    class Test_01():
        def test_01(self, login):
            print('测试内部类')
