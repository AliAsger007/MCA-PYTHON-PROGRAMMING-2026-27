n = abs(int(input("Enter integer: ")))
total = 0
product = 1

while n != 0:
    digit = n % 10
    total += digit
    product *= digit
    n //= 10

print("Sum:", total)
print("Product:", product)
