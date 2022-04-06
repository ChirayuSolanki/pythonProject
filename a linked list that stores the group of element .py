#A python program to create  a linked list and perform operations on the list
list = []
#appending the list
list.append("America")
list.append("India")
list.append("Australia")

#pritning the list
print("Thee existing list : ",list)

# displaying menu
choice = 0
while choice<5 :
    print("Linked list operation. ")
    print("1) Add element.")
    print("2) Remove element ")
    print("3) Replace element")
    print("4) Search element ")
    print("5) Exit")

    choice = int(input("Enter choice : "))

    if choice == 1 :
        element = input("Enter element to add : ")
        pos = int(input("Enter position : "))
        list.insert(pos,element)

    elif choice == 2 :
        try :
            element = input("Enter element to remove : ")
            list.remove(element)
        except ValueError :
            print("Element not found .")

    elif choice == 3 :
        element = input("Enter element to replace : ")
        pos = int(input("Enter position :  "))
        list.pop(pos)
        list.insert(pos,element)

    elif choice == 4 :
        element = input("Enter the element to search : ")

        try :
            pos = list.index(element)
            print("Element found at position . ",pos)
        except ValueError:
            print("Element not found.")
    else :
        break
    # display list
    print("List = ",list)

