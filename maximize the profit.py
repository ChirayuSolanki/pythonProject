# find the maximum profit ??

"""A big company wants to maximize its profit. Therefore, the company hires the product manager.
Now his task is to maximize the profit for the company by travelling and selling products in different cities.
But he has been given with certain conditions. He can travel from city A to city B. In each city he earns some amount of profit,
which is represented by two arrays. Also he has been given with some cost which is travelling cost between two cities.
He can stay in any city during the day or he has an option to move to another city or stay in same city during night. Find the maximum profit."""

# we have given the profit in cities A and B and different locations

# we have to store the profit of city A and city B in two different locations

# And we have given the travelling cost from city A to B

# for finding maximum profit

# making array A

#number of location in city A and B
from array import *
x =  int(input("Locations : "))
a = array("i",[int(i) for i in input("Enter number : ").split()])[:x]
print(a)
b = array("i",[int(i) for i in input("Enter number : ").split()])[:x]
print(b)
cost = int(input("Enter cost : "))
def comparing_index_of_different_array():
    """1)first thing we can do is comparing the elements of two array
     2)the bigger one is added to profit """
    global cost
    maximum_profit= 0
    y = 0

    for i in a :
        print("I = ",i)
        if i>=b[y] :
            sum = i + (i+1)
            print("Sum = sum going from a to a+1 : ",sum)
            sum1 = i + b[y+1] - cost
            print("Sum1 = Sum going from a to b : ",sum1)
            sum2 = b[y] + b[y+1]
            print("sum2 = Sum going from b to b+1",sum2)
            if sum>=sum1:
                maximum_profit = maximum_profit+sum
                print("comparing sum of SUM and Sum1 : ",maximum_profit)
            elif sum >=sum2:
                maximum_profit = maximum_profit+sum
                print("comparing sum of SUM and Sum2 : ", maximum_profit)

            elif  sum1>=sum2 :
                maximum_profit = maximum_profit+sum1
                print("comparing sum of SUM1 and Sum1 : ", maximum_profit)

        elif i<b[y] :
            sum = i + (i+1)
            print("Sum = sum going from a to a+1 : ", sum)
            sum1 = i + b[y + 1] - cost
            print("Sum1 = Sum going from a to b : ", sum1)
            sum2 = b[y] + b[y + 1]
            print("sum2 = Sum going from b to b+1", sum2)
            if sum >= sum1:
                maximum_profit = maximum_profit + sum
                print("comparing sum of SUM and Sum1 : ", maximum_profit)
            elif sum >= sum2:
                maximum_profit = maximum_profit + sum
                print("comparing sum of SUM and Sum2 : ", maximum_profit)

            elif sum1 >= sum2:
                maximum_profit = maximum_profit + sum1
                print("comparing sum of SUM1 and Sum1 : ", maximum_profit)

        y+=1

    print(maximum_profit," is maximum profit !!")



comparing_index_of_different_array()














