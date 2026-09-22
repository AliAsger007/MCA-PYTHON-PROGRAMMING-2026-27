n = int(input("Enter integer: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")
