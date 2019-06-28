# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()  # now = log(now)
# print('--------------')
# print(now)
# f = log(now) # f = log(log(now))
# print(f)
# print('--------------')
# f()

# def log(*text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             func(*args, **kw)
#             print("end")
#         return wrapper
#     return decorator
#
#
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
# now() # now = log('execute')(now)
# print(now)


import time
import functools

def log_time(text):  # 给装饰器log_time()传入一个参数
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("---start---")
            start = time.time()
            fun = func(*args, **kw)
            end = time.time()
            print("the progame %s runned in %s ms" % (func.__name__, (end - start) * 1000))
            print("---end---")
            return fun
        return wrapper
    return decorator  # log_time(text)(f1)

# #先log_time(text) 返回一个decorator 函数，然后再decorator(f1) 在返回一个wrapper函数  至此就是@log_time("xuanxuan,,,") 和接下俩def f1()
@log_time("xuanxuan,you are a beautiful girl!")
def f1(x, y, z):
    time.sleep(2)  # 作用是让函数暂停2s在执行，就是计算函数执行的时间的
    return x + y + z

def main():
    result = f1(2, 3, 4)
    print("the result and the name of this function is {} and {} ".format(result, f1.__name__))

main()
