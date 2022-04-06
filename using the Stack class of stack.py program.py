from stack import Stack
# create empty stack
s = Stack()

#display menu
choice = 0
while choice<5 :
    print("Stack Operation ")
    print("1) Push Operation")
    print("2) Pop Opeeration ")
    print("3) Peep operation")
    print("4) Search operation ")
    print("5) Exit")
    choice = int(input("Your choice: "))

    #perform a task depending on the input
    if choice == 1:
        element = int(input('Enter element : '))
        s.push(element)
    elif choice==2:
        element = s.pop()
        if element == -1:
            print("The Stack is empty .")
        else:
            print("Poped Element is ",element)
    elif choice == 3:
        element=s.peep()
        print("Topmost element is ",element)
    elif choice == 4:
        element = int(input("Enter element "))
        pos = s.search(element)
        if pos == -1:
            print("Stack is empty.")
        elif pos == -2:
            print("Enter element not found")
        else:
            print("Element found at psoition ",pos)
    else:
        break

    print("Stack = ",s.display())


