# This program calculates the sum from 1 to n

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("The sum is:", total)
