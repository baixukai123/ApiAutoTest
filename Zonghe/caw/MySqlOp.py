'''
数据库操作
'''
import pymysql


def connect(db):
    '''
    连接数据库
    :param db:{"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"}
    :return:
    '''
    host = db['ip']
    port = int(db['port'])
    user = db['username']
    name = db['dbName']
    pwd = db['pwd']
    try:
        c = pymysql.connect(host=host, port=port, user=user, password=pwd, database=name, charset='utf8')
        print(f'数据库连接成功:\n\t{host}:{port}')
        return c
    except Exception as e:
        print(f'数据库连接失败:\n\t{e}')
        return None


# 断开连接
def disconnect(c):
    try:
        c.close()
        print('数据库连接已断开')
    except Exception as e:
        print(f'断开数据库连接失败:\n\t{e}')


# 执行sql语句
def execute(c, sql):
    try:
        cursor = c.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        c.commit()  # 提交
        print(f'sql执行成功:\n\t{sql}')
    except Exception as e:
        print(f'sql执行失败:\n\t{sql}\n异常信息:\n\t{e}')


# 测试代码
if __name__ == '__main__':
    c = connect({"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"})
    execute(c, "delete from Member where 'RegName'='小蜜蜂'")
    disconnect(c)
