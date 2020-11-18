'''
注册测试脚本
'''
import pytest

from Zonghe.baw import Member, DbOp
from Zonghe.caw import DataRead

# 数据库操作
# connent = None


@pytest.fixture()
def register(db):
    # 连接
    global connent
    connent = DbOp.connent(db)
    yield
    # 断开
    DbOp.disconnect(connent)


# 注册失败数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/register_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param


# 注册成功数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/register_pass.yaml"))
def pass_data(request):  # 固定写法
    return request.param


# 重复注册数据
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/register_repeat.yaml"))
def repeat_data(request):  # 固定写法
    return request.param


# 注册失败
def test_register_fail(fail_pass, url, baserequests):
    # print(f"测试数据为:{fail_data['casedata']}")
    # print(f"预期结果为为:{fail_data['expect']}")
    register = Member.register(url, baserequests, fail_pass['casedata'])
    assert str(register.json()['msg']) == str(fail_pass['expect']['msg'])
    assert str(register.json()['status']) == str(fail_pass['expect']['status'])
    assert str(register.json()['code']) == str(fail_pass['expect']['code'])


# 注册成功
def test_register_pass(register, pass_data, url, db, baserequests):
    # global connent
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(connent, phone)
    # 发送请求
    register = Member.register(url, baserequests, pass_data['casedata'])
    # 检查响应结果
    assert str(register.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(register.json()['status']) == str(pass_data['expect']['status'])
    assert str(register.json()['code']) == str(pass_data['expect']['code'])
    # 检查实际注册是否成功

    # 清理环境
    DbOp.deleteUser(connent, phone)


# 重复注册
def test_register_repeat(repeat_data, url, db, baserequests):
    phone = repeat_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(connent, phone)
    # 发送请求
    Member.register(url, baserequests, repeat_data['casedata'])
    register = Member.register(url, baserequests, repeat_data['casedata'])
    # 检查响应结果
    assert str(register.json()['msg']) == str(repeat_data['expect']['msg'])
    assert str(register.json()['status']) == str(repeat_data['expect']['status'])
    assert str(register.json()['code']) == str(repeat_data['expect']['code'])
    # 检查实际注册是否成功

    # 清理环境
    DbOp.deleteUser(connent, phone)
