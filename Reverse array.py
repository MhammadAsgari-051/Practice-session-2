
a = [10, 20, 30, 40, 50]

n = len(a)

for i in range(n // 2):
    temp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = temp

print("Reversed array:", a)
