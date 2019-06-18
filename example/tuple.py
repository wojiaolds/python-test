tup = ([1,2,3],'4',6)
if 6 in tup:
    print(123)
print(tup)
tup[0][1] = 's' #虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
print(tup)
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)