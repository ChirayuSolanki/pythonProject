# finding biggest and smallest number in a list
x = []

# entering number of elements
print("How many elements ? : ",end=" ")
n = int(input())

#entering elements
for i in range(n):
    print("Enter number of elements : ",end=" ")
    x.append(int(input()))

#printing the list
print("Your list is : ",x)

# now finding the biggest and smallest element in list
big = x[0]
for i in range(n):
    if x[i]>big:
        big = x[i]

print("The biggest number is : ", big)





















