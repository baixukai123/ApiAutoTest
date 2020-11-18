import pytest

from Zonghe.baw import DbOp, Member
from Zonghe.caw import DataRead

# 数据库操作
@pytest.fixture()
def register(db):
    # 连接
    global connent
    connent = DbOp.connent(db)
    yield
    # 断开
    DbOp.disconnect(connent)


# 注册成功数据(绝对)
@pytest.fixture(params=DataRead.readyaml("Zonghe\data_case\login_register_pass.yaml"))
def ng_data(request):  # 固定写法
    return request.param


# 登录失败数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_fail_none.yaml"))
def fail_none_data(request):  # 固定写法
    return request.param


# 登录成功数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_pass.yaml"))
def pass_data(request):  # 固定写法
    return request.param


# 登录成功
def test_login_pass(register, pass_data, url, db, baserequests):
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(connent, phone)
    # 发送请求
    Member.register(url, baserequests, pass_data['casedata'])
    login = Member.login(url, baserequests, pass_data['casedata'])
    # 检查响应结果
    assert str(login.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(login.json()['status']) == str(pass_data['expect']['status'])
    assert str(login.json()['code']) == str(pass_data['expect']['code'])
    # 清理环境
    DbOp.deleteUser(connent, phone)


# 登录失败（用户名或密码不能为空）
def test_login_fail_none(fail_none_data, url, db, baserequests):
    # 发送请求
    login = Member.login(url, baserequests, fail_none_data['casedata'])
    # 检查响应结果
    assert str(login.json()['msg']) == str(fail_none_data['expect']['msg'])
    assert str(login.json()['status']) == str(fail_none_data['expect']['status'])
    assert str(login.json()['code']) == str(fail_none_data['expect']['code'])


# 登录失败（用户名或密码不正确）
def test_login_pass(register, pass_data, ng_data, url, db, baserequests):
    ng = ng_data['casedata']['mobilephone']
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(connent, ng)
    DbOp.deleteUser(connent, phone)
    # 发送请求
    Member.register(url, baserequests, ng_data['casedata'])
    login = Member.login(url, baserequests, pass_data['casedata'])
    # 检查响应结果
    assert str(login.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(login.json()['status']) == str(pass_data['expect']['status'])
    assert str(login.json()['code']) == str(pass_data['expect']['code'])
    # 清理环境
    DbOp.deleteUser(connent, ng)
