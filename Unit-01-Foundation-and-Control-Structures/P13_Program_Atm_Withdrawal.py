pin = int(input("Enter PIN: "))
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if pin != 1234:
    print("Invalid PIN")
elif amount <= 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
else:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
