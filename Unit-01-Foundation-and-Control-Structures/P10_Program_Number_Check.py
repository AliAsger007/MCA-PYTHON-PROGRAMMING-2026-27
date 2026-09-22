n = int(input("Enter integer: "))

if n == 0:
    print("Zero")
elif n > 0:
    print("Positive")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
