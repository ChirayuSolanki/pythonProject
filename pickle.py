import Emp,pickle
f = open('emp2.dat','wb')
n = int(input("Enter number of employee : "))
for i in range(n):
    id1 = input("Enter Id : ")
    name  = input("Enter name : ")
    salary  = input("Enter salary  : ")

    e = Emp.Emp(id1,name,salary)
    pickle.dump(e,f)
f.close()

