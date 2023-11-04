a = int(input('a = '))
b = int(input('b = '))
op = input('add/sub/multi/div:')
if op == 'add':
    c = a + b
elif op == 'sub':
    c = a - b
elif op == 'multi':
    c = a * b
elif op == 'devi':
    c = a / b
else:
    c = 'Error'
print('Answer = ', c)
