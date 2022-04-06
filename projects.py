def reverse_string():
    flag = True
    while flag :
        n = str(input())
        lst = n.split()
        print(lst)
        newword = [i[ :  : -1] for i in lst]
        newsentence = " ".join(newword)
        print(newsentence)

        if n == " ":
            flag = False
            break

reverse_string()