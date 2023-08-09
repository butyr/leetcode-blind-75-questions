import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs,target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ],
)
def test_solution(inputs, target, expected):
    sut = Solution()

    actual = sut.search(inputs, target)

    assert actual == expected
