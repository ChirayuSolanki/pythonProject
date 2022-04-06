 """Line 1 : The width of the game (the number of stacks of boxes), N, followed by the max height H of each stack.


• Line 2 : N integers, the initial number of boxes in each stack, from left to right. Each number is ≤ H.


• Line 3 : A sequence of integers, each encoding a command to the crane.

    The commands are encoded as follows:

    1 : Move left

    2 : Move right

    3 : Pick up box

    4 : Drop box

    0 : Quit


• The command Quit (0) appears exactly once, and is the last command.

• The initial position of the crane is above the leftmost stack, with the crane not holding any box."""

# N and H seperating by space denoting number of stacks and maximum height of each stack
N,H = [int(i) for i in input("Enter nnumber of stacks ahd height of each stack : ").split()][:2]
stacks = [int(j) for j in input("Enter nummber of boxes : ").split()][:N]
current_position = 0
crane = stacks[current_position]
rules = [int(i) for i in input("Enter : ").split()]
for i in rules:
    if i==2:
        current_position+=1
        print("At right ")
        print(current_position)
        print(crane)

    elif i==1:

        current_position-=15
        print("At left ")

        print(current_position)
        print(crane)

    elif i==3:

        crane = crane-1

        print("pick box ",crane)

        stacks[current_position] = crane
        print(current_position)
        print(crane)

    elif i == 4 :

        crane = crane+1
        print("Drop Box")

        stacks[current_position] = crane
        print(current_position)
        print(crane)

    elif i==0:
        break
print(stacks)

