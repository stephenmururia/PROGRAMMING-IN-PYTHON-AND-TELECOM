i. Prompt user input
name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))

ii. Calculate basic pay
basic_pay = hours_worked * rate_per_hour

iii. Calculate tax based on basic pay
if basic_pay > 50000:
    tax = basic_pay * 0.20
elif basic_pay >= 20000:
    tax = basic_pay * 0.10
else:
    tax = 0

iv. Calculate net pay
net_pay = basic_pay - tax

Display output
print("\n--- Salary Details ---")
print("Employee Name:", name)
print("Basic Pay:", basic_pay)
print("Tax:", tax)
print("Net Pay:", net_pay)
