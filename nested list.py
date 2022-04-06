# to create list as another list as element
list = [10,20,30,40,[80,90]]
print("Total list : ",list)
print("First element of list : ",list[0])
print("Last element of list : ",list[4])
for i in list[4]:
    print("Nested list is : ",i)
