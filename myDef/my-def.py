
import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    return x1, x2


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


'''
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''


def f1(a, b, c=0, *args, e, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'e =', e, 'd =', d, 'kw =', kw)


'''
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
'''


def fun_test(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    for arg in args:
        print(arg, end=" ")
    print()
    print(kwargs.keys())
    print(kwargs.values())


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 利用递归函数移动汉诺塔:
def moveHNT(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        moveHNT(n - 1, a, c, b)
        moveHNT(1, a, b, c)
        moveHNT(n - 1, b, a, c)

moveHNT(4, 'A', 'B', 'C')

print(my_abs(-65.2))
print(math.pi)
print(math.sin(math.pi / 6))
print(math.cos(math.pi / 6))
print(move(3, 4, 9, math.pi / 6))
print(quadratic(1, 2, -3))

f1('s', 1, e='4r', d='fd')
f1(*('s', 1, '5'), e='4r', d='fd')
f1('s', 1, '5', 5, 'tg', e='4r', d='fd')
fun_test(*(1, 'r', 3, 'd'), user='lds', **{'url': 'www.baidu.com', 'passwd': 'lds1992'})

print(fact(12))

def trim(s):
    if(s[0] == ' '):
        s = s[1:]
    if(s[-1] == ' '):
        s = s[:-1]
    return s

print("a",end='')
print(trim(" sdf "),end='')
print("b")