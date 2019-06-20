def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)

print(r.__next__())
print(list(r))

def my_map(f,l):
    for i in l:
        yield f(i)

m = my_map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(m)
print(list(m))
print(list(my_map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9])))


