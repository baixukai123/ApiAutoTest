'''
读文件
'''
import configparser
import os

import yaml


def getProjectPath():
    '''
    获取当前工程路径
    :return:
    '''
    current_file_path = os.path.realpath(__file__)  # 当前文件路径
    # print(current_file_path)
    dir_name = os.path.dirname(current_file_path)  # 文件所在目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)  # 上级目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)  # 上级目录
    return dir_name + "\\"


def readini(filePath, key):
    '''
    读取ini文件
    :param filePath: 文件路径
    :param key: ini中关键字
    :return: key对应的value
    '''
    real_path = getProjectPath() + filePath
    # 调用ConfigParser来解析配置文件
    config = configparser.ConfigParser()
    # 读文件
    config.read(real_path)
    # env表示section,根据key在对应的section中取value
    value = config.get("env", key)
    return value


def readyaml(filePath):
    '''
    读取yaml文件
    :param filePath:文件路径
    :return: yaml文件内容
    '''
    path = getProjectPath() + filePath  # 拼接完整路径
    with open(path, 'r', encoding='utf-8') as f:  # 打开文件
        load = yaml.load(f, Loader=yaml.FullLoader)  # 读取文件内容，放置到变量load中
        return load


# if __name__ == '__main__':
#     # 预期返回D:\手工测试\LearnPytest\
#     print(getProjectPath())
#     # 预期返回http://jy001:8081/
#     r = readini(r"ZongHe\data_env\env.ini", "url")
#     print(r)
#     d = readyaml(r"Zonghe\data_case\register_fail.yaml")
#     print(d)
