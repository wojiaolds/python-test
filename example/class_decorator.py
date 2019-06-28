from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            print(self)
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        print('logit只打日志，不做别的')
        pass



class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super().__init__(*args, **kwargs)

    def notify(self):
        print('发送一封email到self.email')
        # 这里就不做实现了
        pass

class logit1(object):
    def __init__(self, func):
        self.logfile = 'out2.log'
        self.fun = func


    def __call__(self,*args, **kwargs):

        print(self)
        log_string = self.fun.__name__ + " was called"
        print(log_string)
        # 打开logfile并写入
        with open(self.logfile, 'a') as opened_file:
            # 现在将日志打到指定的文件
            opened_file.write(log_string + '\n')
        # 现在，发送一个通知
        self.notify()
        return self.fun(*args, **kwargs)


    def notify(self):
        print('logit只打日志，不做别的')
        pass

@logit1
def myfunc():
    print('myfunc end')


@logit()
def myfunc1():
    print('myfunc1 end')

@email_logit('email','out1.log')
def myfunc2():
    print('myfunc2 end')


myfunc1()
print('----'*10)
myfunc2()
print('----'*10)
myfunc()

print('----'*10)

print(myfunc1)
print(myfunc2)
print(myfunc)

