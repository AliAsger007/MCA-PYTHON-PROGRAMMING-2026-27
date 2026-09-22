gb = float(input("Enter data usage in GB: "))

if gb <= 5:
    bill = 199
elif gb <= 10:
    bill = 299
elif gb <= 20:
    bill = 399
else:
    bill = 499

print("Total Bill:", bill)
