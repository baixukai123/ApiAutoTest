'''
监控代码：内存、cpu、网络、磁盘等，与项目部署到一起
'''
from datetime import datetime

import psutil
from time import sleep

#
# print("cpu信息:\n\t", psutil.cpu_percent())  # 获取cpu信息
# print("虚拟内存:\n\t", psutil.virtual_memory())  # 虚拟内存
# print("虚拟内存占比:\n\t", psutil.virtual_memory().percent)  # 内存百分比
# print("项目所在磁盘:\n\t", psutil.disk_usage("d:/"))  # 项目所在磁盘
# print("项目所在磁盘占比:\n\t", psutil.disk_usage("d:/").percent)  # 项目所在磁盘占比
# print("网络:\n\t", psutil.net_io_counters())  # 网络
# print("发送字节数:\n\t", psutil.net_io_counters().bytes_sent)  # 发送字节数
# print("接收字节数:\n\t", psutil.net_io_counters().bytes_recv)  # 接收字节数

with open('D:/资源占用监控。txt', encoding='utf-8', mode='a') as file:
    # strfime 当前时间转为字符串
    file.write("日期:\t"+datetime.strftime(datetime.now(), "%Y-%m-%d")+"\n")
    file.write("时间戳\t\tCPU\t\t内存\t磁盘\t发送\t\t接收\t\n")
    while True:
        # strfime 当前时间转为字符串
        file.write(datetime.strftime(datetime.now(), "%H:%M:%S") + "\t")
        file.write(str(psutil.cpu_percent()) + '%\t')
        file.write(str(psutil.virtual_memory().percent) + '%\t')
        file.write(str(psutil.disk_usage("d:/").percent) + '%\t')
        file.write(str(psutil.net_io_counters().bytes_sent) + '\t')
        file.write(str(psutil.net_io_counters().bytes_recv) + '\t\n')
        file.flush()  # 从缓存写入文件
        sleep(1)
