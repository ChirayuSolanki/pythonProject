# a python program to solve tower of hanoni problem
def tower(disks,pole_A,pole_C,pole_B):
    if disks==1:
        # if only one disk than move it from a to c
        print("move disk %i from %s to %s"%(disks,pole_A,pole_C))
    else:
        # if more than one disk
        #move first n-1 disks form a to b as c intermediate pole
        tower(disks-1,pole_A,pole_B,pole_C)
        print("move disk %i from pole %s to  %s" % (disks, pole_A, pole_C))

        #move disk n-1 from pole b to pole c as pole a a intermediate
        tower(disks-1,pole_B,pole_C,pole_A)

# calling the function
n = int(input("Enter number  of disks : "))


tower(n,'pole A','pole C','pole B')

