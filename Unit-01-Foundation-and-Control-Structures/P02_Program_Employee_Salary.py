basic = float(input("Enter basic salary: "))

da = basic * 0.10
hra = basic * 0.20
gross = basic + da + hra
tax = gross * 0.10
net = gross - tax

print("DA:", da)
print("HRA:", hra)
print("Gross Salary:", gross)
print("Tax:", tax)
print("Net Salary:", net)
