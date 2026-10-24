
a = [10,0, 20, 30, 40, 50]

maximum = a[0]

for v in a[1:]:
    if v > maximum:
        maximum = v

print("Maximum:", maximum)
