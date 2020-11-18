'''
性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape

'''
为要模拟的用户定义一个类，从HttpUser继承
'''


class CarRental(HttpUser):
    # between 是user累中定义的方法
    # wait_time是user类定义的属性，表示等待时间
    wait_time = between(3, 8)  # 任务与任务之间的等待时间在3，8之间取随机数

    @task
    def loadAllRent(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")


# -f 要执行的文件
# --host 被测系统
# --web-host local web页面的地址
# --web-prot local web页面的端口
# locust -f Zonghe\locust_test.py --host=http://localhost:8080 --web-host=http://localhost -prot=8089
# --step-load阶梯式加压


# class StepLoadShape(LoadTestShape):
#     """
#     A step load shape
#
#
#     Keyword arguments:
#
#         step_time -- Time between steps
#         step_load -- User increase amount at each step
#         spawn_rate -- Users to stop/start per second at every step
#         time_limit -- Time limit in seconds
#
#     """
#
#     step_time = 30
#     step_load = 10
#     spawn_rate = 10
#     time_limit = 600
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         if run_time > self.time_limit:
#             return None
#
#         current_step = math.floor(run_time / self.step_time) + 1
#         return (current_step * self.step_load, self.spawn_rate)


# class StagesShape(LoadTestShape):
#     """
#     A simply load test shape class that has different user and spawn_rate at
#     different stages.
#
#     Keyword arguments:
#
#         stages -- A list of dicts, each representing a stage with the following keys:
#             duration -- When this many seconds pass the test is advanced to the next stage
#             users -- Total user count
#             spawn_rate -- Number of users to start/stop per second
#             stop -- A boolean that can stop that test at a specific stage
#
#         stop_at_end -- Can be set to stop once all stages have run.
#     """
#
#     stages = [
#         {"duration": 60, "users": 10, "spawn_rate": 10},
#         {"duration": 100, "users": 50, "spawn_rate": 10},
#         {"duration": 180, "users": 100, "spawn_rate": 10},
#         {"duration": 220, "users": 30, "spawn_rate": 10},
#         {"duration": 230, "users": 10, "spawn_rate": 10},
#         {"duration": 240, "users": 1, "spawn_rate": 1},
#     ]
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 tick_data = (stage["users"], stage["spawn_rate"])
#                 return tick_data
#
#         return None


class DoubleWave(LoadTestShape):
    """
    A shape to immitate some specific user behaviour. In this example, midday
    and evening meal times.

    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
    """

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 60

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                    (self.peak_one_users - self.min_users)
                    * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                    + (self.peak_two_users - self.min_users)
                    * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                    + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None
