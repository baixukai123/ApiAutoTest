import pytest

from Zonghe.baw import Member, DbOp
from Zonghe.caw import DataRead


# 登录数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_data.yaml"))
def login_data(request):  # 固定写法
    return request.param


# 登陆前置数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_setup.yaml"))
def setup_data(request):  # 固定写法
    return request.param


# 测试前后置
@pytest.fixture()
def register(setup_data, url, baserequests, db):
    connent = DbOp.connent(db)
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(connent, phone)
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除
    DbOp.deleteUser(connent, phone)
    DbOp.disconnect(connent)


def test_login(register, login_data, url, baserequests):
    # 登录
    # 检查的登录结果
    member_login = Member.login(url, baserequests, login_data['casedata'])
    assert member_login.json()['msg'] == login_data['expect']['msg']
