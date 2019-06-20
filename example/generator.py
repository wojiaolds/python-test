# from collections import Iterable
def my_for(g):
    for i in g:
        print(i)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


g = (x * x for x in range(10))
print(list(g))

# print(isinstance(g, Iterable))
# print(g.__next__())
# print(g.__next__())
# print(next(g))
# print(next(g))

# my_for(g)


f = fib(6)
print(f)
my_for(f)

def triangles():
    L1 = [1]
    L2 = [1,1]
    L3 = []
    yield L1
    yield L2
    while True:
        L3.append(1)
        i = 0;
        l = len(L2)
        while i < l-1:
            L3.append(L2[i]+L2[i+1])
            i = i+1
        L3.append(1)
        yield L3
        L2 = L3
        L3 = []

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

