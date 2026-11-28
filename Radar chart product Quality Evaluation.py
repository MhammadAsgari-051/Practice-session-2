
import numpy as np
import matplotlib.pyplot as plt

categories = ["Price","Durability","Safety","Quality","Energy Saving"]

quality = [7, 9, 10, 8, 9]

angles = np.linspace(
    0, 2 * np.pi, len(categories), endpoint=False
).tolist()

quality += [quality[0]]
angles += [angles[0]]

fig, ax = plt.subplots(
    figsize=(7, 7),
    subplot_kw={"polar": True}
)

ax.plot(angles, quality, marker="o", linewidth=2)
ax.fill(angles, quality, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

ax.set_ylim(0, 10)
ax.set_title("Product Quality Evaluation")

plt.show()
