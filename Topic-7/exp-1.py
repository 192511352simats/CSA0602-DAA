def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    m = n // 2
    a, b = [r[:m] for r in A[:m]], [r[m:] for r in A[:m]]
    c, d = [r[:m] for r in A[m:]], [r[m:] for r in A[m:]]
    e, f = [r[:m] for r in B[:m]], [r[m:] for r in B[:m]]
    g, h = [r[:m] for r in B[m:]], [r[m:] for r in B[m:]]

    M1 = strassen(add(a,d), add(e,h))
    M2 = strassen(add(c,d), e)
    M3 = strassen(a, sub(f,h))
    M4 = strassen(d, sub(g,e))
    M5 = strassen(add(a,b), h)
    M6 = strassen(sub(c,a), add(e,f))
    M7 = strassen(sub(b,d), add(g,h))

    C11 = add(sub(add(M1,M4),M5),M7)
    C12 = add(M3,M5)
    C21 = add(M2,M4)
    C22 = add(sub(add(M1,M3),M2),M6)

    return [C11[i]+C12[i] for i in range(m)] + \
           [C21[i]+C22[i] for i in range(m)]

def multiply(A, B):
    n = 1
    size = max(len(A), len(A[0]), len(B), len(B[0]))
    while n < size:
        n *= 2

    P = [[0]*n for _ in range(n)]
    Q = [[0]*n for _ in range(n)]

    for i in range(len(A)):
        for j in range(len(A[0])):
            P[i][j] = A[i][j]

    for i in range(len(B)):
        for j in range(len(B[0])):
            Q[i][j] = B[i][j]

    C = strassen(P, Q)
    return [r[:len(B[0])] for r in C[:len(A)]]

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

print("Result:")
for row in multiply(A,B):
    print(row)
