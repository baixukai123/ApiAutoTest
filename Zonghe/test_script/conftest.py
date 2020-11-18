'''
脚本层公共方法
'''
import pytest

from Zonghe.baw import DbOp
from Zonghe.caw import DataRead
from Zonghe.caw.BaseRequests import BaseRequests


# 从环境文件中读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.readini("Zonghe\data_env\env.ini", 'url')


# 从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    # 将从ini中读取的字符串转为字典，使用eval函数
    return eval(DataRead.readini("Zonghe\data_env\env.ini", 'db'))


# 创建BaseRequests的一个实例
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()


# # 数据库操作
# @pytest.fixture(scope='function')
# def register(db):
#     # 连接
#     global connent
#     connent = DbOp.connent(db)
#     yield
#     # 断开
#     DbOp.disconnect(connent)
