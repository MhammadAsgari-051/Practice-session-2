
import matplotlib.pyplot as plt

time = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

pressure = [1.0, 1.3, 1.7, 2.1, 2.5,
            2.8, 2.6, 2.3, 1.9, 1.5]

plt.figure(figsize=(9, 5))

plt.plot(time, pressure, marker="o")

plt.xlabel("Time (Minutes)")
plt.ylabel("Pressure (Bar)")
plt.title("Water Tank Pressure Changes")

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
