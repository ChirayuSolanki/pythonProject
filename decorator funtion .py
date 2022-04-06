# a decorator that increment the value of a funciton by 2
def decor(fun) :
    def inner():
        value = fun()
        return value + 2
    return inner

# take a function to which decorator should be applied
def num() :
    return 10

#call decorator function and passing the num
result_fun = decor(num)
print(result_fun())


