def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    high1, low1 = divmod(x, p)
    high2, low2 = divmod(y, p)

    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba(low1 + high1, low2 + high2) - z2 - z0

    return z2*p*p + z1*p + z0


assert karatsuba(1234,5678) == 1234*5678
assert karatsuba(123456789,987654321) == 123456789*987654321
assert karatsuba(9,9) == 81
assert karatsuba(0,12345) == 0
