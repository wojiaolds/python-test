def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
print(f1()) #9
print(f2()) #9
print(f3()) #9


def creatCounter():
    def f():
        x = 0
        while True:

            x = x + 1
            print(x)
            yield x
    sum = f()  #返回生成器
    print(sum)
    def counter():
        print('lds')
        return next(sum)

    return counter
countA = creatCounter()
countA()
countA()
print(countA(),countA(),countA())
print(creatCounter()(),creatCounter()(),creatCounter()())

print("-------------------")
j =0
def creatCounter():
    s = [0,1]
 
    def counter():

        s[0] = s[0] + 1

        return s[0]

    return counter

c= creatCounter()
print("--------------")
print(c(),c(),c())

h = 0;
print(id(h))
h = h+1  # 地址已变
print(id(h))