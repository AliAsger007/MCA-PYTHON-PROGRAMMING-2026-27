while True:
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter number: "))
        prime = True

        if n < 2:
            prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break

        print("Prime" if prime else "Not Prime")

    elif choice == 2:
        n = int(input("Enter number: "))
        original = n
        reverse = 0

        while n != 0:
            reverse = reverse * 10 + n % 10
            n //= 10

        print("Palindrome" if original == reverse else "Not Palindrome")

    elif choice == 3:
        n = int(input("Enter number: "))
        original = n
        digits = len(str(abs(n)))
        total = 0

        while n != 0:
            total += (n % 10) ** digits
            n //= 10

        print("Armstrong" if total == original else "Not Armstrong")

    elif choice == 4:
        n = int(input("Enter number: "))
        factorial = 1

        for i in range(1, n + 1):
            factorial *= i

        print("Factorial:", factorial)

    elif choice == 5:
        n = int(input("Enter terms: "))
        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        print()

    elif choice == 6:
        break

    else:
        print("Invalid Choice")
