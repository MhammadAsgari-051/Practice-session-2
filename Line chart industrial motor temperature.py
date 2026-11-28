
import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temperature = [25, 28, 32, 35, 39, 43, 47, 51, 55, 60]

plt.figure(figsize=(9, 5))

plt.plot(time, temperature, marker="o")

plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (C)")
plt.title("Industrial Motor Temperature")

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
