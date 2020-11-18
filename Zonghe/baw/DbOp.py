'''
数据库操作
    数据库从mysql换成sqlite，脚本层不用改动，只用改动caw里的mysql.py以及此文件
    此部分访问到业务的数据库，所以放在baw中
'''
from Zonghe.caw import MySqlOp

def connent(db):
    return MySqlOp.connect(db)

def deleteUser(conn, phone):
    '''
    根据手机号删除用户
    :param db: 字典存储数据库信息
    :param phone: 手机号
    :return:
    '''
    sql = f'delete from Member where MobilePhone={phone}'
    MySqlOp.execute(conn, sql)

def disconnect(conn):
    MySqlOp.disconnect(conn)


# if __name__ == '__main__':
#     deleteUser({"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"}, 15111111111)
