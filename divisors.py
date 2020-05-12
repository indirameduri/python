'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you dont know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

num = int(input('Enter a number: '))

l=[]

for i in range(1,num+1):
    if(num % i == 0):
        l.append(i)
        
print('All the divisors for {} are = {}'.format(num,l))
    