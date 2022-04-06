# a python program to calculate the net salary and gross salary of an employee

def dearness_allowance(basics):
    """da is the 80% of basic salary"""
    da1 = basics*80/100
    return da1

def home_rent_allowance(basics):
    """Hra is the  15% of basics salary"""
    HRA = basics*15/100
    return HRA

def provident_fund(basics):
    "pf is the 12% of basic salary"
    pf = basics*12/100
    return pf

def income_tax(basics):
    "income tax is the 10% of gross income"
    income_tax = gross_salary*0.1
    return income_tax

#this is the main program
basic_salary = float(input("Enter your basic salary : "))

gross_salary = basic_salary+dearness_allowance(basic_salary)+home_rent_allowance(basic_salary)
print("Your Gross Salary is : ",gross_salary)

net_salary =gross_salary-provident_fund(basic_salary)-income_tax(basic_salary)
print("Your Net Salary is : ",net_salary)