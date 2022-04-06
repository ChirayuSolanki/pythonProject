#displaying list element in reversr order
days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "saturday"]
print(days)
# now displaying in reverse order
print("\nIn reverse order")
i=len(days)-1
while i>=0:
    print(days[i])
    i-=1



print("\nIn reverse order")
i=-1
while i>=-len(days):
    print(days[i])
    i-=1


