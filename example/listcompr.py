L = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L if isinstance(s,str)])

print( [x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

print(list(range(2,9)))