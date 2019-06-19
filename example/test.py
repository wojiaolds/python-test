i = 1
print(i, id(i))
i = 2
print(i, id(i))

s = [0]
print(s, id(s))


def f():
    s[0] = s[0] + 1

    print(s, id(s))

    # print(s, id(s))
    print(i, id(i))


f()

s = '12345'
# s[0] = 'd' #不能修改
print(s, id(s))

s = 'wsdeef'
print(s, id(s))

l = [1, 2, 'sde']
print(l, id(l))

l[0] = 'dede'
# l[2][1] = '3' #不能修改
l[2] = '233ed'
print(l, id(l))

tup = (1, 2, 'des')
print(tup, id(tup))

# tup[0] = 'e' #不能修改
tup = ()
print(tup, id(tup))

dict = {'a': 1, 'b': 'sdds'}
print(dict, id(dict))

dict['a'] = 'dwed'
print(dict, id(dict))

dict['b'] = 'dwed'
print(dict, id(dict))

s1 = dict['b']
print(dict, id(dict))
print(dict['b'], id(dict['b']))
print(s1, id(s1))
try:
    s1[0] = '3' #不能修改
except Exception as e:
    print(e)
print('------------------------')
dict['b'] = 'dsc'
print(dict, id(dict))
print('------------------------')
dict['b'] = [1,3]
print(dict, id(dict))
print(s1, id(s1))
print('------------------------')
s1 = dict['b']
print(s1, id(s1))
print('------------------------')
s1[0]='ewd'
print(s1, id(s1))
print(dict, id(dict))
print(dict['b'], id(dict['b']))
print('------------------------')
dict['b'][0] = 362
print(dict, id(dict))
print(s1, id(s1))
print(dict['b'], id(dict['b']))


