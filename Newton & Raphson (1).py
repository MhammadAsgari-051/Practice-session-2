def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x = float(input("Enter initial guess: "))
tolerance = 1e-6
max_iter = 100

for i in range(max_iter):
    if abs(f(x)) < tolerance:
        break
    x = x - f(x) / df(x)

print(f"Root found: {x}")
print(f"Iterations: {i}")