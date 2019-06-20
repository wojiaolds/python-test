def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):

    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

def is_palindrome(n):
    s = str(n)
    l = len(s)
    i = 0
    j = -1
    while i < l//2:
        if s[i] != s[j]:
            return False
        i,j = i+1,j-1
    return True

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
l = list(filter(is_palindrome, range(1, 200)))
if l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print(l)
    print('测试成功!')
else:
    print(l)
    print('测试失败!')

