import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("A man, a plan, a canal: Panama", True),
    ]
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.is_palindrome(inputs)

    assert actual == expected
