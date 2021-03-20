

a = 'My name is %s and i am %s ' %('abc', '17')
print(a)

r = '1: {one}, 2: {two}'.format(one=111, two=222)
print(r)

t1 = 123
t2 = 456 

k = '1: {1}, 2: {0}'.format(t1, t2)
print(k)