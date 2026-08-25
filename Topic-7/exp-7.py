def schoolbook(x, y):
    result = 0
    for i, a in enumerate(str(x)[::-1]):
        for j, b in enumerate(str(y)[::-1]):
            result += int(a) * int(b) * 10**(i+j)
    return result


for digits in [2,4,8,16,32]:
    x = int('7' * digits)
    y = int('3' * digits)

    assert karatsuba(x,y) == schoolbook(x,y)

    print("Digits:", digits,
          "Schoolbook:", schoolbook(x,y),
          "Karatsuba:", karatsuba(x,y))
