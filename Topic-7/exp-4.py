import random
import time

for n in [8,16,32]:

    A=[[random.randint(1,10) for _ in range(n)] for _ in range(n)]
    B=[[random.randint(1,10) for _ in range(n)] for _ in range(n)]

    t=time.time()
    standard_multiply(A,B)
    standard=time.time()-t

    t=time.time()
    strassen(A,B)
    strassen_time=time.time()-t

    print(n, "Standard:", standard, "Strassen:", strassen_time)
