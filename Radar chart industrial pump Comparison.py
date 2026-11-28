
import numpy as np
import matplotlib.pyplot as plt

categories = [
    "Flow Rate",
    "Pressure",
    "Efficiency",
    "Reliability",
    "Noise"
]

pump_A = [8, 7, 9, 8, 6]
pump_B = [7, 9, 7, 9, 8]

angles = np.linspace(
    0, 2 * np.pi, len(categories), endpoint=False
).tolist()

pump_A += [pump_A[0]]
pump_B += [pump_B[0]]
angles += [angles[0]]

fig, ax = plt.subplots(
    figsize=(8, 8),
    subplot_kw={"polar": True}
)

ax.plot(angles, pump_A, marker="o", label="Pump A")
ax.fill(angles, pump_A, alpha=0.15)

ax.plot(angles, pump_B, marker="o", label="Pump B")
ax.fill(angles, pump_B, alpha=0.15)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

ax.set_ylim(0, 10)
ax.set_title("Industrial Pump Comparison")
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

plt.show()
