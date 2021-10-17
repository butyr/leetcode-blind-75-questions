import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.product_except_self(inputs)

    assert actual == expected
