# Enter your code here. Read input from STDIN. Print output to STDOUT
# a function to test wheather a number is prime or not

import time, math
prime_num=[2]

def calculate_all_prime(input_number):
    """to check wheather if integer_number is prime or not"""
    print(time.time())
    flag = True
    startVal = 2
    for x in range(3,input_number,2):
        print("startVal",startVal)
        for i in range(startVal, x):
            if startVal != 2  and (startVal >= math.floor(x/2) and x>5):
                flag = False
                break
            elif x % i == 0:
                flag = False
                break
            else:
                flag = True

        if flag:
            print(x)
            startVal = x
            prime_num.append(x)

    print(time.time())

def prime_sum(curr_num):
    if curr_num == 1:
        return 0
    elif curr_num == 2:
        return 2
    else:
        sum = 0
        for prime in prime_num:
            if prime > curr_num:
                break
            sum = sum + prime

        return sum


n = int(input())
num = []
for i in range(0, n):
    num.append(int(input()))

calculate_all_prime(sorted(num)[len(num)-1])

for i in range(0, len(num)):
    print(prime_sum(num[i]))