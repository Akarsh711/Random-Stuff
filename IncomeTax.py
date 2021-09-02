gross_income = float(input("Enter the gross income"))

dependents = int(input("Enter he number of dependents"))

taxable_income = gross_income - 10000 - 3000 * dependents

income_tax = taxable_income * 0.20

print("The income rate is "+str(income_tax))