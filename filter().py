# welocoming user and asking number between 1 to 1000 and finding its even or odd
def odd_even():
    print("Enter number you have in your box ? : ")
    y = int(input())

    if y >= 1 and y <= 1000 :

        flag = True
        if y%2==0 :
            print(y , " is even. Have another ?? ")
            if odd_even():
                flag = True
            else :
                flag = False

        else :
            print(y," is odd.Have another ?? ")
            if odd_even():
                flag = True
            else :
                flag = False
    else:
        print("Sorry , you haven't enter number between 1 to 1000")

# calling function
x = odd_even()
