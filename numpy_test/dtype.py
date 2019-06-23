#int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
import numpy as np

dt = np.dtype('i4')
print(dt)

dt = np.dtype([('age', np.int8)])
print(dt)
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print(a['age'])

student = np.dtype([('name', 'S20'),  ('age',  'i1'),  ('marks',  'f4')])
a = np.array([('abc',  21,  50), ('xyz',  18,  75)], dtype=student)
print(student)
print(a)

