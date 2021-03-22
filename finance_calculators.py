import math
#this is an import that allow access to math functions

calculator_choice = input("Choose either 'investment' or 'bond' from the menu below to proceed:\ninvestment  - to calculate the amount of interest you'll earn on interest.\nbond  - to calculate the amount you'll have to pay on a home loan.\n")

ignore_lettercase = calculator_choice.casefold()
#user input is made to compatable by ignoring variation.

if ignore_lettercase == "investment":
    money_deposit = float(input("Enter the amount of money that you are depositing:\n"))
    interest_rate = float(input("Enter the interest rate:\n"))
    cal_interest_rate = interest_rate / 100
    number_of_years = float(input("Enter the number of years you plan to invest for:\n"))
    interest = input("Do you want SIMPLE or COMPOUND interest:\n")
    #the above user input is used to do a calculation of interest and distinguishes between simple or compound interest.
    if interest == "simple":
        simple_interest = money_deposit * (1 + cal_interest_rate * number_of_years)
        print("Your investment with simple interest is R{}.".format(math.floor(simple_interest)))
    elif interest == "compound":
        compound_interest = money_deposit * math.pow((1 + cal_interest_rate),number_of_years)
        print("Your investment with compound interest is R{}.".format(math.floor(compound_interest)))

#These are the fomulas for the calculations:
#The total amount when simple interest is applied is calculated as follows: A = P(1 + r * t)
#The Python equivalent is very similar: A =P*(1+r*t)
#The total amount when compound interest is applied is calculated as follows: A = P(1 + r) ^ t
#The Python equivalent is slightly different: A = P* math.pow((1+r),t)
#r is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
#P is the amount that the user deposits.
#t is the number of years that the money is being invested for.
#A is the total amount once the interest has been applied.


        
        
elif ignore_lettercase == "bond":
    house_value = float(input("What is the present value of the house:\n"))
    interest_rate = float(input("Enter the interest rate:\n"))
    cal_interest_rate = (interest_rate / 100)/12
    number_of_months = float(input("Enter the number of months you plan to repay the bond:\n"))
    bond_repayment = (cal_interest_rate * house_value) / (1 - math.pow((1+cal_interest_rate),(-number_of_months)))
    print("Your bond repayment per month is: R{}.".format(math.floor(bond_repayment)))
                                                          
#This is the fomula for the calculation:  
#The amount that a person will have to be repaid on a home loan each month is calculated as follows: repayment = (i.P)/(1 - (1+i)^(-n))
#P is the present value of the house.
#i is the monthly interest rate, calculated by dividing the annual interest rate by 12.
#n is the number of months over which the bond will be repaid.
        
                          

