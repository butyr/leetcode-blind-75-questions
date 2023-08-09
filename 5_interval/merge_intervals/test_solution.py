import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]][[1, 5]],),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.merge(inputs)

    assert actual == expected
