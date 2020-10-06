from cProfile import run
from timeit import timeit
from FastFisher import FisherExact


tests = ((539, 468),
         (1000, 500),
         (2000, 500),
         (2000, 1000),
         (3000, 500),
         (3000, 1000),
         (3000, 2000),
         (3000, 3000),
         (4000, 500),
         (4000, 1000),
         (4000, 2000),
         (4000, 3000),
         (4000, 4000),
         (10000, 9000),
         (20000, 19900))

for a, b in tests:
    m = (a + b + 1) // 2
    print(f'FisherExact({m}, {a}, {m}, {b}) = ', end="")
    print(" and took {:.4f}s".format(
        timeit("print('{:.6f}'.format("
               f"FisherExact({m}, {a}, {m}, {b})), end='')",
               setup="from __main__ import FisherExact",
               number=1)))
