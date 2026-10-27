
# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

# Calculate gross salary
gross = basic + allowances + overtime + incentives

# Calculate deductions
pf = basic * 0.12
professional_tax = 200

# Progressive tax calculation (illustrative slabs)
if gross <= 10000:
    income_tax = 0
elif gross <= 20000:
    income_tax = (gross - 10000) * 0.05
else:
    income_tax = 10000 * 0.05 + (gross - 20000) * 0.10

total_deductions = pf + professional_tax + income_tax
net_salary = gross - total_deductions

# Formatted salary statement
print("\n" + "=" * 40)
print("         EMPLOYEE SALARY STATEMENT")
print("=" * 40)
print(f"Employee Name      : {name}")
print(f"Employee ID        : {emp_id}")
print("-" * 40)
print(f"Basic Pay          : Rs. {basic:,.2f}")
print(f"Allowances         : Rs. {allowances:,.2f}")
print(f"Overtime Pay       : Rs. {overtime:,.2f}")
print(f"Incentives         : Rs. {incentives:,.2f}")
print("-" * 40)
print(f"Gross Salary       : Rs. {gross:,.2f}")
print("-" * 40)
print(f"Provident Fund     : Rs. {pf:,.2f}")
print(f"Professional Tax   : Rs. {professional_tax:,.2f}")
print(f"Income Tax         : Rs. {income_tax:,.2f}")
print(f"Total Deductions   : Rs. {total_deductions:,.2f}")
print("-" * 40)
print(f"NET SALARY         : Rs. {net_salary:,.2f}")
print("=" * 40)
