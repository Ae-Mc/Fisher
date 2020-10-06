from decimal import Decimal


def Binominal(n: int, k: int) -> int:
    result = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        result *= n - i
        result //= i + 1
    return result


def pvalue(a: int, b: int,
           c: int, d: int) -> Decimal:
    return (Decimal(Binominal(a + b, a)
                    * Binominal(c + d, c))
            / Decimal(Binominal(a + b + c + d, a + c)))


def FisherLeftSide(a: int, b: int,
                   c: int, d: int,
                   baseP: Decimal) -> Decimal:
    p = Decimal(0)
    curP = baseP
    while(a > 0 and d > 0):
        curP *= a * d
        a -= 1
        b += 1
        c += 1
        d -= 1
        curP /= b * c
        if curP <= baseP:
            p += curP
    return p


def FisherRightSide(a: int, b: int,
                    c: int, d: int,
                    baseP: Decimal) -> Decimal:
    p = Decimal(0)
    curP = baseP
    while(b > 0 and c > 0):
        curP *= b * c
        a += 1
        b -= 1
        c -= 1
        d += 1
        curP /= a * d
        if curP <= baseP:
            p += curP
    return p


def FisherExact(a: int, b: int,
                c: int, d: int,
                two_tailed: bool = True) -> Decimal:
    p = t = pvalue(a, b, c, d)
    p += FisherLeftSide(a, b, c, d, t)
    if two_tailed:
        p += FisherRightSide(a, b, c, d, t)
    return p
