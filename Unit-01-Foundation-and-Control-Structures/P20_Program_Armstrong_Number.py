n = int(input("Enter integer: "))
original = n
digits = len(str(abs(n)))
total = 0

while n != 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
