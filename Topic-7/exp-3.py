import random
import time


# ==========================================================
# STANDARD MATRIX MULTIPLICATION
# ==========================================================

def standard_multiply(A, B):
    n = len(A)
    m = len(B)
    p = len(B[0])

    C = [[0] * p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C


# ==========================================================
# MATRIX ADDITION
# ==========================================================

def add_matrix(A, B):
    n = len(A)
    m = len(A[0])

    return [
        [A[i][j] + B[i][j] for j in range(m)]
        for i in range(n)
    ]


# ==========================================================
# MATRIX SUBTRACTION
# ==========================================================

def subtract_matrix(A, B):
    n = len(A)
    m = len(A[0])

    return [
        [A[i][j] - B[i][j] for j in range(m)]
        for i in range(n)
    ]


# ==========================================================
# STRASSEN MULTIPLICATION
# ==========================================================

def strassen_multiply(A, B):
    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide A
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide B
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Seven Strassen products
    M1 = strassen_multiply(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    M2 = strassen_multiply(
        add_matrix(A21, A22),
        B11
    )

    M3 = strassen_multiply(
        A11,
        subtract_matrix(B12, B22)
    )

    M4 = strassen_multiply(
        A22,
        subtract_matrix(B21, B11)
    )

    M5 = strassen_multiply(
        add_matrix(A11, A12),
        B22
    )

    M6 = strassen_multiply(
        subtract_matrix(A21, A11),
        add_matrix(B11, B12)
    )

    M7 = strassen_multiply(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    # Calculate result matrices
    C11 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M4),
            M5
        ),
        M7
    )

    C12 = add_matrix(M3, M5)

    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M3),
            M2
        ),
        M6
    )

    # Combine
    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


# ==========================================================
# FIND NEXT POWER OF TWO
# ==========================================================

def next_power_of_two(n):
    power = 1

    while power < n:
        power *= 2

    return power


# ==========================================================
# PAD MATRIX WITH ZEROS
# ==========================================================

def pad_matrix(A, rows, cols):
    padded = []

    for i in range(rows):
        row = []

        for j in range(cols):
            if i < len(A) and j < len(A[0]):
                row.append(A[i][j])
            else:
                row.append(0)

        padded.append(row)

    return padded


# ==========================================================
# STRASSEN FOR ARBITRARY SIZE MATRICES
# ==========================================================

def strassen_arbitrary_size(A, B):

    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    # Check dimensions
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions are incompatible")

    # Find required padded size
    size = max(rows_A, cols_A, rows_B, cols_B)

    padded_size = next_power_of_two(size)

    # Pad matrices
    A_padded = pad_matrix(
        A,
        padded_size,
        padded_size
    )

    B_padded = pad_matrix(
        B,
        padded_size,
        padded_size
    )

    # Strassen multiplication
    C_padded = strassen_multiply(
        A_padded,
        B_padded
    )

    # Remove extra rows and columns
    C = [
        C_padded[i][:cols_B]
        for i in range(rows_A)
    ]

    return C


# ==========================================================
# RANDOM MATRIX
# ==========================================================

def random_matrix(rows, cols):
    return [
        [random.randint(1, 10) for _ in range(cols)]
        for _ in range(rows)
    ]


# ==========================================================
# BENCHMARK
# ==========================================================

def benchmark(n):

    A = random_matrix(n, n)
    B = random_matrix(n, n)

    # Standard multiplication
    start = time.perf_counter()

    standard_multiply(A, B)

    standard_time = time.perf_counter() - start

    # Strassen multiplication
    start = time.perf_counter()

    strassen_multiply(A, B)

    strassen_time = time.perf_counter() - start

    return standard_time, strassen_time

A5 = [[i + j for j in range(5)] for i in range(5)]
B5 = [
    [1 if i == j else 0 for j in range(5)]
    for i in range(5)
]
assert strassen_arbitrary_size(A5, B5) == standard_multiply(A5, B5)
A_rect = [
    [1, 2, 3],
    [4, 5, 6]
]
B_rect = [
    [7, 8],
    [9, 10],
    [11, 12]
]
assert strassen_arbitrary_size(A_rect, B_rect) == standard_multiply(A_rect, B_rect)
print("Question 3: All test cases passed!")
A, B = random_matrix(8, 8), random_matrix(8, 8)
assert strassen_multiply(A, B) == standard_multiply(A, B)
print("Question 4: Correctness test passed!")
for n in [8, 16, 32, 64]:

    std_t, strassen_t = benchmark(n)

    print(
        f"{n}x{n} -> "
        f"Standard: {std_t:.6f} sec, "
        f"Strassen: {strassen_t:.6f} sec"
    )
std_t, strassen_t = benchmark(16)
assert std_t >= 0
assert strassen_t >= 0

print("All test cases passed!")
