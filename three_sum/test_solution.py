import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.three_sum(inputs)

    assert actual == expected
