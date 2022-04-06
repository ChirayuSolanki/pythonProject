# dequeu data structure
from collections import deque
d = deque()

choice = 0
while choice<7:
    print("DEQUE OPERATION")
    print("1 Add element at the front.")
    print("2 Delete element at the front.")
    print("3 Add element at the back.")
    print("4 Delete element at the back.")
    print("5 remove element from the middle.")
    print("6 Search for element")
    print("7 Exit")
    choice = int(input('Your choice : '))

    # perform a task depending upon user choice
    if choice==1 :
        element= input("Enter element : ")
        d.appendleft(element)
    elif choice == 2:
        if len(d) == 0:
            print("Deque iws empty.")
        else:
            d.popleft()
    elif choice == 3:
        element = input("Enter element : ")
        d.append(element)
    elif choice == 4 :
        if len(d) == 0 :
            print("Deque is Empty")
        else:
            d.pop()
    elif choice == 5:
        element = input("Enter element : ")
        try :
            d.remove(element)
        except ValueError :
            print("Element not found .")
    elif choice == 6  :
        element = input("Enter element to serach : ")
        c = d.count(element)
        print("Number of times the element found : ",c)
    else:
        break

    print('Deque = ',end='')
    for i in d:
        print(i,' ',end='')
    print()