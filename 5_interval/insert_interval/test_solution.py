import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, new_interval, expected",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[3, 5], [6, 7], [8, 10]],
        ),
    ],
)
def test_solution(inputs, new_interval, expected):
    sut = Solution()

    actual = sut.insert(inputs, new_interval)

    assert actual == expected
