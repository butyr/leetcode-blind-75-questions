import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([0], True),
        ([], False),
        ([2, 1, 1], True),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 5, 0, 0], True),
        ([1, 1, 2, 2, 0, 1, 1], True),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], True),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.can_jump(inputs)

    assert actual == expected
