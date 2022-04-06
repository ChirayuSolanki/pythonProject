# a python project that give user freedom to select what type of information(related to salary) they have and can find all other type of salary,tax,
#allowance they can have
#dearness_allowance,provident_fund,home_rent_allowance,gross_salary
A = "Dearness allowance"
B = "Provident fund"
C = "Home rent allowance"
D = "Gross salary"
E = "Basic salary"


print("What type of information do you have ?\nA)Dearness allowance    B)Provident fund     C)Home rent allowance      E)Basic salary : ")
x = input("Enter : ")
user_input = x.upper()

#starting fnction
#if user have basic salary
if user_input=="E":
    def dearness_allowance(basics):
        """da is the 80% of basic salary"""
        da1 = basics * 80 / 100
        return da1


    def home_rent_allowance(basics):
        """Hra is the  15% of basics salary"""
        HRA = basics * 15 / 100
        return HRA


    def provident_fund(basics):
        "pf is the 12% of basic salary"
        pf = basics * 12 / 100
        return pf


    def income_tax(basics):
        "income tax is the 10% of gross income"
        income_tax = gross_salary * 0.1
        return income_tax


    # this is the main program
    basic_salary = float(input("Enter your basic salary : "))

    gross_salary = basic_salary+dearness_allowance(basic_salary)+home_rent_allowance(basic_salary)
    print("Your gross salary is : ",gross_salary)
    print("Dearness allowance : ",dearness_allowance(basic_salary))
    print("Provident fund",provident_fund(basic_salary))
    print("income tax",income_tax(basic_salary))
    print("home rent allowance : ",home_rent_allowance(basic_salary))


#otherwise of A
elif user_input=="A":
    """then it will be dearness allowance and you have to find basic salary and use employee module """
    dearness_allowance = float(input("Enter dearness allowance : "))
    basic_salary = dearness_allowance*100/80
    from employee import *
    gross_salary = basic_salary+provident_fund(basic_salary)+home_rent_allowance(basic_salary)
    print("Your gross salary is : ", gross_salary)
    print("Your gross salary is : ", gross_salary)
    print("Provident fund", provident_fund(basic_salary))
    print("income tax", income_tax(basic_salary))
    print("home rent allowance : ", home_rent_allowance(basic_salary))


#otherwise B
elif user_input=="B":
    """Then it will be provident fund """
    provident_fund = float(input("Enter dearness allowance  : "))
    basic_salary = provident_fund*100/12
    from employee import*
    gross_salary = basic_salary+provident_fund(basic_salary)+home_rent_allowance(basic_salary)  
    home_rent_allowance(basic_salary)
    income_tax(gross_salary)
    dearness_allowance(basic_salary)
    print("Your gross salary is : ", gross_salary)
    print("Dearness allowance : ", dearness_allowance(basic_salary))
    print("income tax", income_tax(basic_salary))
    print("home rent allowance : ", home_rent_allowance(basic_salary))

#othwrwise C
elif user_input=="C":
    """Then it will be Home rent allowance """
    Home_rent_allowance = float(input("Enter Home rent allowance  : "))
    basic_salary = Home_rent_allowance*100/15
    print("Your basic salary is : ",basic_salary)
    from employee import*
    gross_salary = basic_salary+provident_fund(basic_salary)+home_rent_allowance(basic_salary)
    print("Gross salary : ",gross_salary)
    print("Your gross salary is : ", gross_salary)
    print("Dearness allowance : ", dearness_allowance(basic_salary))
    print("Provident fund", provident_fund(basic_salary))
    print("income tax", income_tax(basic_salary))

