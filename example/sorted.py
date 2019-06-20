print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21],key=abs))

def my_sorted(l):
    i = 0;
    l_len = len(l)
    while i < l_len-1:
        j = i+1
        while j < l_len:
            if(l[j] < l[i]):
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
            j =j+1
        i = i+1

    return l

my_list = [36, 5, -12, 9, -21]
print(my_sorted(my_list))
print(my_list)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str.lower(t[0])
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
print(L2)
print(L)
L3 = sorted(L, key=by_score,reverse=True)
print(L3)
print(L)


