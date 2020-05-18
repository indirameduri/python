'''
Fibonacci series
'''

num = int(input('Enter a number'))

a = c = 0
b = 1 

for i in range(num):
    a = b
    b = c
    c = a+b
    print(c)