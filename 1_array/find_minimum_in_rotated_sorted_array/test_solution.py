import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.findMin(inputs)

    assert actual == expected
