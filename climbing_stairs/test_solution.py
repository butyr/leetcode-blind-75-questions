import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (3, 3),
        (5, 8),
        (10, 89),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.climb_stairs(inputs)

    assert actual == expected
