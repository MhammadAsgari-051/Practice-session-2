
n = 8

triangle = []

for i in range(n + 1):
    row = []

    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            number = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(number)

    triangle.append(row)

for row in triangle:
    print(row)
