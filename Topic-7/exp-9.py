def karatsuba_traced(x, y, trace=None, depth=0):
    if trace is None:
        trace = []

    if x < 10 or y < 10:
        trace.append((depth, x, y, None, None, None, None))
        return x*y, trace

    n = max(len(str(x)), len(str(y)))
    m = n//2
    p = 10**m

    a,b = divmod(x,p)
    c,d = divmod(y,p)

    trace.append((depth, x, y, a, b, c, d))

    z0,_ = karatsuba_traced(b,d,trace,depth+1)
    z2,_ = karatsuba_traced(a,c,trace,depth+1)
    z1,_ = karatsuba_traced(a+b,c+d,trace,depth+1)

    z1 = z1-z2-z0

    return z2*p*p+z1*p+z0, trace


result, trace = karatsuba_traced(1234,56)

assert result == 1234*56
assert len(trace) > 0
assert trace[0][0] == 0

print("Result:", result)
print("Trace:")
for t in trace:
    print(t)

