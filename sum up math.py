
x = float(input("Enter x: "))
y = float(input("Enter y: "))

a = x + y

if a == 0:
    print("The series is undefined")
else:
    s = 0

    for n in range(101):
        s = s + 1 / (a ** n)

    print("Sum =", s)
