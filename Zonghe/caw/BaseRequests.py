'''
对requests中的get、post的方法进行封装
1、增加异常处理
2、增加日志打印
3、创建一个session，确保能自动管理cookie
'''
import requests


class BaseRequests:
    def __init__(self):
        # 创建一个session，赋值给session
        self.session = requests.session()

    # 重写get方法
    def get(self, url, **kwargs):
        try:
            # 使用session的方式调用requests中的get接口
            session_get = self.session.get(url, **kwargs)
            print(f"发送get请求:{url},参数:{kwargs}成功")
            return session_get
        except Exception as e:
            print(f"发送get请求:{url},参数:{kwargs}异常，异常信息为:{e}")

    # 重写post方法
    def post(self, url, **kwargs):
        try:
            # 使用session的方式调用requests中的post接口
            session_post = self.session.post(url, **kwargs)
            print(f"发送post请求:{url},参数:{kwargs}成功")
            return session_post
        except Exception as e:
            print(f"发送post请求:{url},参数:{kwargs}异常，异常信息为:{e}")


# # 测试代码，用完可注掉
# if __name__ == '__main__':
#     print(BaseRequests().get('http://www.httpbin.org/get?username=root&pwd=123123').text)
#     print(BaseRequests().post('http://www.httpbin.org/post?username=root&pwd=123123').text)
