
import matplotlib.pyplot as plt

expenses = ["Salary", "Rent", "Electricity", "Transport", "Other"]
costs = [5000, 2000, 800, 1200, 1000]

plt.figure(figsize=(8, 6))

plt.pie(
    costs,
    labels=expenses,
    autopct="%1.1f%%",
    explode=[0.05, 0, 0, 0, 0]
)

plt.title("Monthly Company Expenses")
plt.show()
