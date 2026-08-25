def standard_multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def sub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def strassen_hybrid(A, B, threshold=2):
    n = len(A)

    if n <= threshold:
        return standard_multiply(A, B)

    m = n // 2

    A11=[r[:m] for r in A[:m]]
    A12=[r[m:] for r in A[:m]]
    A21=[r[:m] for r in A[m:]]
    A22=[r[m:] for r in A[m:]]

    B11=[r[:m] for r in B[:m]]
    B12=[r[m:] for r in B[:m]]
    B21=[r[:m] for r in B[m:]]
    B22=[r[m:] for r in B[m:]]

    M1=strassen_hybrid(add(A11,A22),add(B11,B22),threshold)
    M2=strassen_hybrid(add(A21,A22),B11,threshold)
    M3=strassen_hybrid(A11,sub(B12,B22),threshold)
    M4=strassen_hybrid(A22,sub(B21,B11),threshold)
    M5=strassen_hybrid(add(A11,A12),B22,threshold)
    M6=strassen_hybrid(sub(A21,A11),add(B11,B12),threshold)
    M7=strassen_hybrid(sub(A12,A22),add(B21,B22),threshold)

    C11=add(sub(add(M1,M4),M5),M7)
    C12=add(M3,M5)
    C21=add(M2,M4)
    C22=add(sub(add(M1,M3),M2),M6)

    return [C11[i]+C12[i] for i in range(m)] + \
           [C21[i]+C22[i] for i in range(m)]

import random

A=[[random.randint(-5,5) for _ in range(4)] for _ in range(4)]
B=[[random.randint(-5,5) for _ in range(4)] for _ in range(4)]

assert strassen_hybrid(A,B,2) == standard_multiply(A,B)
assert strassen_hybrid(A,B,4) == standard_multiply(A,B)

print("All test cases passed!")
