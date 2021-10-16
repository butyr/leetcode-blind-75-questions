import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.length_of_longest_substring(inputs)

    assert actual == expected
