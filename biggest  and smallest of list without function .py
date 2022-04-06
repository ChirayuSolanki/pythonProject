# finding biggest and smallest element in a list without using built-in function
lst = []

print("How many elements : ",end=" ")
user_input = int(input())

for i in range(user_input):
    print("Enter elements : ",end=" ")
    lst.append(int(input()))

print("The list is : ",lst)

big= lst[0]
small = lst[0]

for i in range(1,user_input):  #repeat from 1 to n-1
    #big
    if lst[i]>big :
        big = lst[i]
    #small
    if lst[i]<small :
        small = lst[i]

print("Maximum is : ",big)
print("Minimum is :",small)
