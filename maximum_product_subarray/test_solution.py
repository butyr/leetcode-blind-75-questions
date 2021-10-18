import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([2, 3, -2, 4], 6),
        ([-2, 2, 3, 4], 24),
        ([-2, 2, 3, 4, -1], 48),
    ]
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.max_product(inputs)

    assert actual == expected
