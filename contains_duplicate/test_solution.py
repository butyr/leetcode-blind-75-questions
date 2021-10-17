import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.contains_duplicate(inputs)

    assert actual == expected
