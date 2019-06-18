import math

def quadratic(a, b, c):
    x1 = (-b+math.sqrt(math.pow(b,2)-4*a*c))/2*a
    x2 = (-b-math.sqrt(math.pow(b,2)-4*a*c))/2*a
    return x1,x2


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

print(my_abs(-65.2))
print(math.pi)
print(math.sin(math.pi/6))
print(math.cos(math.pi/6))
print(move(3,4,9,math.pi/6))
print(quadratic(1,2,-3))

