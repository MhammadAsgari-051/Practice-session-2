A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

def determinant(matrix):

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    total = 0

    for j in range(n):

        minor = []

        for i in range(1, n):
            row = matrix[i][:j] + matrix[i][j+1:]
            minor.append(row)

        total += ((-1) ** j) * matrix[0][j] * determinant(minor)

    return total

def cofactor_matrix(matrix):

    n = len(matrix)
    cofactors = []

    for i in range(n):

        row = []

        for j in range(n):

            minor = []

            for r in range(n):

                if r != i:
                    new_row = matrix[r][:j] + matrix[r][j+1:]
                    minor.append(new_row)

            value = ((-1) ** (i+j)) * determinant(minor)

            row.append(value)

        cofactors.append(row)

    return cofactors

print("Original Matrix:")

for row in A:
    print(row)

C = cofactor_matrix(A)

print("\nCofactor Matrix:")

for row in C:
    print(row)

print("\nDeterminant =", determinant(A))
