from fractions import gcd

def jugs(a, b, c):
    # Edge Cases
    if c > a and c > b:
        return False
    if a == b:
        if a == c:
            return True
        else:
            return False

    d = gcd(a, b)
    if c % d == 0:
        return True
    else:
        return False

print(jugs(131, 264, 30))
print(jugs(972, 79, 506))
print(jugs(504, 858, 147))
print(jugs(797, 612, 939))
print(jugs(799, 678, 227))


