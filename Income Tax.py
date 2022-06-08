#Income Tax Calculations

t=int(input())
for i in range(t):
    annual_income=int(input("Enter your income:"))
    hra=int(input("Enter your hra:"))
    deductions=int(input("Enter other deductions:"))
    taxable_amt=annual_income-hra*12-deductions*12

    if(taxable_amt<300000):
        print("Income tax to be paid is 0")
    elif(taxable_amt>300000 and taxable_amt<600000):
        print("Income tax to be paid is",taxable_amt*0.10)
    elif(taxable_amt>600000 and taxable_amt<1000000):
        print("Income tax to be paid is",taxable_amt*0.15)
    else:
        print("Income tax to be paid is",taxable_amt*0.20)
    