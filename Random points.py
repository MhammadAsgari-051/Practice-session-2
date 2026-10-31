
import random
import math

# Create 15 random points
points = []

for i in range(15):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)

    points.append((x, y))

# Find the shortest distance
min_distance = float("inf")

for i in range(15):
    for j in range(i + 1, 15):

        x1, y1 = points[i]
        x2, y2 = points[j]

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        if distance < min_distance:
            min_distance = distance
            point1 = points[i]
            point2 = points[j]

# Print results
print("Random points:")

for point in points:
    print(point)

print("Shortest distance =", min_distance)
print("First point =", point1)
print("Second point =", point2)
