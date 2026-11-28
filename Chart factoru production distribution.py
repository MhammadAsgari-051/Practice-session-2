
import matplotlib.pyplot as plt

products = ["Product A", "Product B", "Product C", "Product D"]

production = [1200, 800, 1500, 500]

plt.figure(figsize=(8, 6))

plt.pie(
    production,
    labels=products,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Factory Production Distribution")
plt.show()
