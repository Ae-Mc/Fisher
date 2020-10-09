import pytest
from FisherExactTest import FisherExact
from decimal import Decimal


@pytest.mark.parametrize("table, expected", [
    ([[100, 2], [1000, 5]], 0.1300759363430016),
    ([[2, 100], [5, 1000]], 0.1300759363430016),
    ([[2, 7], [8, 2]], 0.0230141375652212),
    ([[5, 1], [10, 10]], 0.1973244147157191),
    ([[5, 15], [20, 20]], 0.0958044001247763),
    ([[5, 16], [20, 25]], 0.1725864953812995),
    ([[10, 5], [10, 1]], 0.1973244147157192),
    ([[10, 5], [10, 0]], 0.0612648221343874),
    ([[5, 0], [1, 4]], 0.0476190476190476),
    ([[0, 5], [1, 4]], 1),
    ([[5, 1], [0, 4]], 0.0476190476190476),
    ([[0, 1], [3, 2]], 1),
    ([[19950, 20000], [19950, 19000]], 0.0003228308460000)
])
def test_two_tailed_Fisher_exact_test(table, expected):
    epsilon = Decimal("1e-10")
    expected = Decimal(expected)
    p = FisherExact(table[0][0], table[0][1], table[1][0], table[1][1])
    assert abs(p - expected) < epsilon
