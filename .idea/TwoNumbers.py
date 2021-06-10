num1 = 1.5
num2 = 6.3
sum = num1 + num2

print('Sum of {0} and {1} is {2} '.format(num1,num2,sum))
print('')

# sum two numbers by user inputs

num3 = input('Enter some number : ')
num4 = input('Enter any number : ')
sums = float(num3) + float(num4)

print('The sum of {0} and {1} is {2}'.format(num3,num4,sums))

# generate random number

import random
print('')
print('Prints random number between 0 and 9')
print(random.randint(0,9))

#square root for positives numbers
print('')
num = 9

num_sqrt = num ** 0.5
print('The square root of %0.2f is %0.2f'%(num,num_sqrt))

#complex numbers
print('')
import cmath

num = 1+2j

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.2f} + {2:0.2f}'.format(num,num_sqrt.real,num_sqrt.imag))