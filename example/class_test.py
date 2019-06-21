

class Animal(object):
    # 用tuple定义允许绑定的属性名称
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    __slots__ = ('sex')

    def run(self):
        print('I\'m is a Animal')

'''
实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性；
不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''
class Dog(Animal):
    # 用tuple定义允许绑定的属性名称
    # 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    __slots__ = ('name', 'age','_Dog__name','fun','set_age')
    count = 0 # 类属性
    def __init__(self,name):
        self.__name = name #实例属性
        Dog.count += 1
    def __len__(self):
        return 1
    def run(self):
        print('I\'m is a Dog')

    def get_name(self):
        return self.__name

print(dir(str))

dog = Dog('jack')
dog.sex = 'male'
print(id(dog))
dog = Dog('jack')
print(id(dog))

print('dog count:',Dog.count)

def fun(self):
    print(self,'fun')

dog.fun = fun  #动态绑定方法
dog.fun(123)

# dog = Dog('jack')
# # dog.fun(234) # 给一个实例绑定的方法，对另一个实例是不起作用的

def set_age(self, age):
    self.age = age
from types import MethodType
dog.set_age = MethodType(set_age, dog)  # 给实例绑定一个方法
dog.set_age(10)
print(dog.age)


dog.name = 34 #动态绑定属性
# 不是同一个属性
print(dog.get_name())
print(dog.name)

print(dir(dog))

print(len(dog)) # 在len()函数内部，它自动去调用该对象的__len__()方法

print(list(range(2)))
