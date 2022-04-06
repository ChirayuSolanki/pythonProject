#save this code as employee.py

def dearness_allowance(basics):
    """da is the 80% of basic salary"""
    da1 = basics*80/100
    return da1

def home_rent_allowance(basics):
    """HRA is the  15% of basics salary"""
    HRA = basics*15/100
    return HRA

def provident_fund(basics):
    "pf is the 12% of basic salary"
    pf = basics*12/100
    return pf

def income_tax(gross_salary):
    "income tax is the 10% of gross income"
    income_tax = gross_salary*0.1
    return income_tax
