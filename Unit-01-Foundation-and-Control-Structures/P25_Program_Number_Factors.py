n = int(input("Enter integer: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        count += 1

print("Total Factors:", count)
