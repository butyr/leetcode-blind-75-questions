import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.max_profit(inputs)

    assert actual == expected
