n = abs(int(input("Enter integer: ")))

count = 0
largest = 0
smallest = 9

if n == 0:
    count = 1
    largest = 0
    smallest = 0
else:
    while n != 0:
        digit = n % 10
        count += 1
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        n //= 10

print("Number of Digits:", count)
print("Largest Digit:", largest)
print("Smallest Digit:", smallest)
