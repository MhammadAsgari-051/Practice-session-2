import numpy as np
import matplotlib.pyplot as plt

def generate_coral_reef(iterations=300_000, burn_in=100, seed=42):
    rng = np.random.default_rng(seed)
    x, y = 0.0, 0.0
    points = np.empty((iterations, 2), dtype=np.float32)

    for i in range(iterations + burn_in):
        r = rng.random()

        if r < 0.40:
            new_x = 0.31*x - 0.53*y + 0.89
            new_y = -0.46*x - 0.29*y + 1.04

        elif r < 0.55:
            new_x = 0.31*x - 0.08*y + 0.22
            new_y = 0.15*x - 0.45*y + 0.34

        else:
            new_x = 0.55*y + 0.01
            new_y = 0.69*x - 0.20*y + 0.38

        x, y = new_x, new_y

        if i >= burn_in:
            points[i - burn_in] = (x, y)

    return points


if __name__ == "__main__":

    points = generate_coral_reef()

    plt.figure(figsize=(8, 8))
    plt.scatter(points[:, 0], points[:, 1], s=0.08)

    plt.title("Coral Reef - Chaos Game (IFS)")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()

    plt.show()