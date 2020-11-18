'''
任务集合:分层，按模块子系统管理
'''
from locust import TaskSet, task, HttpUser, between


class SystemManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/sys/toUserManager.action")

    @task
    def task2(self):
        self.client.get("/carRental/sys/toRoleManager.action")

    @task
    def task3(self):
        self.client.get("/carRental/sys/toLogInfoManager.action")


# 基础管理模块
class BasicManage(TaskSet):
    @task(9)
    def task1(self):
        self.client.get("/carRental/bus/toCustomerManager.action")

    @task(1)
    def task2(self):
        self.client.get("/carRental/bus/toCarManager.action")


class CarRentalTest(HttpUser):
    wait_time = between(1, 3)  # 任务间的时间间隔
    # tasks = [BasicManage, SystemManage]  # 任务集合 tasks是User中定义的属性，不能写错
    tasks = {BasicManage: 9, SystemManage: 1}  # 任务集合（加权） tasks是User中定义的属性，不能写错

    def on_start(self):  # 测试前置
        user = {"loginname": "admin", "pwd": "123456"}
        self.client.post("/carRental/login/login.action", data=user)

    def on_stop(self):  # 测试后置
        self.client.post("/carRental/强行退出登录")

# -f 要执行的文件
# --host 被测系统
# --web-host local web页面的地址
# --web-prot local web页面的端口
# locust -f Zonghe\locust_test02.py --host=http://localhost:8080 --web-host=http://localhost -prot=8089
