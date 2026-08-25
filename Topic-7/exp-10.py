def multiply_polynomials_naive(a,b):
    result = [0]*(len(a)+len(b)-1)

    for i in range(len(a)):
        for j in range(len(b)):
            result[i+j] += a[i]*b[j]

    return result


def add_poly(a,b):
    n=max(len(a),len(b))
    return [
        (a[i] if i<len(a) else 0) +
        (b[i] if i<len(b) else 0)
        for i in range(n)
    ]


def karatsuba_poly(a,b):
    if len(a)==1:
        return [a[0]*x for x in b]

    n=max(len(a),len(b))
    m=(n+1)//2

    a += [0]*(m-len(a))
    b += [0]*(m-len(b))

    a0,a1=a[:m],a[m:]
    b0,b1=b[:m],b[m:]

    z0=karatsuba_poly(a0,b0)
    z2=karatsuba_poly(a1,b1)
    z1=karatsuba_poly(add_poly(a0,a1),add_poly(b0,b1))

    z1=add_poly(add_poly(z1,[-x for x in z0]),[-x for x in z2])

    result=[0]*(2*m)

    for i,x in enumerate(z0):
        result[i]+=x

    for i,x in enumerate(z1):
        result[i+m]+=x

    for i,x in enumerate(z2):
        result[i+2*m]+=x

    return result


assert multiply_polynomials_naive([1,2],[3,4]) == [3,10,8]

p1=[1,2,3,4]
p2=[5,6,7,8]

naive=multiply_polynomials_naive(p1,p2)
kar=karatsuba_poly(p1,p2)[:len(naive)]

assert kar == naive
