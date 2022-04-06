from sympy import *
def prime_sum():
    x = int(input())
    sum = 2
    for i in range(3,x,2):
        if isprime(i) == True :
            sum = sum + i
    print(sum)

n = int(input())
for i in range(n):
    prime_sum()