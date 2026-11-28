
import numpy as np
import matplotlib.pyplot as plt

categories = [ "Power",  "Speed","Efficiency","Accuracy","Stability"]

values = [8, 9, 7, 8, 6]

angles = np.linspace(
    0, 2 * np.pi, len(categories), endpoint=False
).tolist()

values += [values[0]]
angles += [angles[0]]

fig, ax = plt.subplots(
    figsize=(7, 7),
    subplot_kw={"polar": True})

ax.plot(angles, values, marker="o")
ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

ax.set_ylim(0, 10)
ax.set_title("Electric Motor Performance")

plt.show()
