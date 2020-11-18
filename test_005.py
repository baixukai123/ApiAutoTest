'''
mark标记
1、skip：此版本有缺陷，导致某个用例不通过，先跳过，待缺陷修复后再执行
2、自定义标记
    代码规模大，测试用例多，只想执行其中某部分代码，定义标记
'''
import pytest


def test01():
    print('测试用例1')


@pytest.mark.skip(reason="有缺陷，缺陷号为001，带缺陷解决后再执行")
def test02():
    print('测试用例2')


@pytest.mark.maoyan
def test03():
    print('测试用例3')


@pytest.mark.api
class TestUserMark:
    @pytest.mark.maoyan
    def test04(self):
        print('测试用例1')

    def test05(self):
        print('测试用例2')

    def test06(self):
        print('测试用例3')
