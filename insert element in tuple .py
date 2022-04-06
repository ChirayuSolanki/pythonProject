# fibonnaci sequence
"""You are given with a N integer and you need to find the sum upto Nth fibonaaci term."""
#Firtly,input contain "t" denoting no. of test cases.Each test case will have an positive number N
# 1<=t<=10
# 1<=N<=30
# fibonaaci sequence : it start with zero and 1 and then then another is created by adding two previous number

"""***** Logic_of_fibonaaci_sequence ******
# two logic 1)first to take all the fibonnacio number to 30 than make logic using that
#2)and second to take logic of fiibonaaci number and use it ."""
# choosing second
""""""


def fibonaaci_squence():
    """Fibonaaci Logic : *) store two permanants value that is n1 = 0,n2 = 1
     *)after adding this two number update the value of variable n1 and n2"""
    N = int(input())
    n1,n2 = 0,1
    count = 0
    sum = 0
    if 1<=N<=30:
        while count<N:

            nth = n1 + n2
            sum+=n1
            # update value
            n1 = n2
            n2 = nth
            count+=1
        print(sum)


# test cases
t = int(input())

for i in range(0,t):
    if 1<=t<=10 :
        fibonaaci_squence()