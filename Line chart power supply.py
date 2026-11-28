
import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

voltage = [12.0, 12.1, 11.9, 12.0, 12.2,
           11.8, 12.0, 12.1, 11.9, 12.0]

plt.figure(figsize=(9, 5))

plt.plot(time, voltage, marker="o")

plt.axhline(y=12, linestyle="--", label="Reference Voltage")

plt.xlabel("Time (Seconds)")
plt.ylabel("Voltage (V)")
plt.title("Power Supply Voltage Stability")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
