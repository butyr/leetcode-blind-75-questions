import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]])],
)
def test_solution(inputs, expected):
    sut = Solution()

    sut.set_zeroes(inputs)

    assert inputs == expected
