import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 1], 2),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.maxArea(inputs)

    assert actual == expected
