import copy

a = ['dog', 'cat', 'rabbit', 'duck']
b = copy.copy(a)
print('b = ', b)

b.sort()
print('b = ', b)

print('a = ', a)

