print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('1s3'.encode('ascii'))
print('1s3'.encode('utf-8'))
print('1s3.#&'.encode('utf-8'))
print('刘灯松'.encode('utf-8'))  #在bytes中，无法显示为ASCII字符的字节，用\x##显示。
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('<p>'.encode('utf-8'))
print('<p>'.encode('ascii'))

print('\xa0'.encode('utf-8'))