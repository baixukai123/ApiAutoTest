'''
conftest.py session级别的fixture放在此文件中,文件名固定写法

作用域:本文件夹(首次调用先执行前置,此目录下所有文件执行完执行后置)
'''

import pytest


@pytest.fixture(scope='session')
def login():
    print("登入")
    yield
    print("登出")


@pytest.fixture()
def login1():
    print("登入1")
    yield
    print("登出1")
