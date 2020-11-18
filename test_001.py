'''
测试前后置
模块级和函数级通常一起使用
'''


def setup_module():
    print("测试前置:登录")


def teardown_module():
    print("测试后置:登出")


# 使用setup一样的效果
def setup_function():
    print("测试前置:每个函数前执行一次")


# 使用teardown一样的效果
def teardown_function():
    print("测试后置:每个函数后执行一次")


def test_001():
    print("测试重充值功能用例1")


def test_002():
    print("测试重充值功能用例2")


def test_003():
    print("测试重充值功能用例3")

'''
测试前后置
类和方法级别
'''
class Test001:
    def setup_class(self):
        print("测试前置:类内方法执行前调用")

    def teardown_class(self):
        print("测试后置:类内方法执行后调用")

    def setup_method(self):
        print("测试前置(类):登录")

    def teardown_method(self):
        print("测试后置(类):登出")

    def test_001(self):
        print("用例1")

    def test_002(self):
        print("用例2")

    def test_003(self):
        print("用例3")
