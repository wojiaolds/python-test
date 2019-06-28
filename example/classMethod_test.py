class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)

a = A()

print(a.foo)
print(a.class_foo)
print(a.static_foo)

print('----'*10)
a.foo(1)
# A.foo(1)
A.foo(a,1)
print('----'*10)
A.class_foo(1)
a.class_foo(1)
print('----'*10)
A.static_foo(1)
a.static_foo(1)

class B(A):
    pass
print('----'*10)
b = B()
b.foo(1)
b.class_foo(1)
b.static_foo(1)