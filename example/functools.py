# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
#
# print(now)


# import functools
import time
from collections import Iterable
import types

def log2(text=None):
    def decorator(func):
        # @functools.wraps(func)
        def wrapper(*args,**kw):
            print(type(text))
            print(type(text) == types.FunctionType)
            if isinstance(text,Iterable):
                print('%s begin call %s():' %(text,func.__name__))
                func(*args,**kw)
                print('%s end call %s():' %(text,func.__name__))
            else:
                print('begin call %s():' % func.__name__)
                func(*args,**kw)
                print('end call %s():' % func.__name__)
            return
        return wrapper
    return decorator if isinstance(text,(int,str)) else decorator(text)

@log2
def now2():
    print('now is:'+time.asctime())

now2()

@log2('timeshow')
def now3():
    print('now is:'+'2017-07-10')

now3()

