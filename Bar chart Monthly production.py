
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

production = [1200, 1500, 1100, 1800, 2000, 1700]

plt.figure(figsize=(9, 5))

plt.bar(months, production)

plt.xlabel("Month")
plt.ylabel("Number of Products")
plt.title("Monthly Factory Production")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()
