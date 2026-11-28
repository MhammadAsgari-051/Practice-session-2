
import matplotlib.pyplot as plt

machines = ["Motor 1", "Motor 2", "Pump", "Compressor", "Fan"]

consumption = [350, 280, 190, 420, 120]

plt.figure(figsize=(9, 5))

plt.bar(machines, consumption)

plt.xlabel("Machines")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Industrial Machines Energy Consumption")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()
