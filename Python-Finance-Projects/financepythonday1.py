def main():
    Payback = int(input("Amount of money to be pay back?"))
    print("The amount to be paid back is", Payback)
    InterestRate = float(input("Interest Rate"))
 
LoanAmount = int(input("Principal Amount"))
Payback = InterestRate * LoanAmount


#this the first of my loan management system using the knowlegde i have learnt so far in the cs50P course i have done like 1hr44mins
name = input("Name of borrower?")
Payback = input("Amount of money to be pay back?")
Collateral = input("What is the collateral?")
name = name.strip().title()
Collateral = Collateral.strip().title()
print(f"Customer Details, {name}")
print(f"{LoanAmount}")
print(f"{Payback}")
print(f"{Collateral}")

main()
