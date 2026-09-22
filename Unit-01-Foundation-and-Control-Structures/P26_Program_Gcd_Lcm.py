a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
