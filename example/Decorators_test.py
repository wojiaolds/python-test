def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'

print(id(hi))
print(hi)
print(id(greet))
print(greet)

print('-----'*10)
del hi  #删除了函数的引用   函数本身执行代码还在
# print(id(hi))
# print(hi)
print(id(greet))
print(greet)

print(greet())


