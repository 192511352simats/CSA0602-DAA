def karatsuba_with_count(x, y, counter):
    counter[0] += 1

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    a,b = divmod(x,p)
    c,d = divmod(y,p)

    z0 = karatsuba_with_count(b,d,counter)
    z2 = karatsuba_with_count(a,c,counter)
    z1 = karatsuba_with_count(a+b,c+d,counter)-z2-z0

    return z2*p*p + z1*p + z0


counter = [0]

result = karatsuba_with_count(1234,5678,counter)

assert result == 1234*5678
assert counter[0] > 0

counter2 = [0]
karatsuba_with_count(9,9,counter2)

assert counter2[0] == 1

print("Recursive calls:", counter[0])
