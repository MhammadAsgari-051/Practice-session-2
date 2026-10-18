import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    total += 1.0 / i

print(total)