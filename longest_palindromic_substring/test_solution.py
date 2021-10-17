import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("babad", "bab"),
        ("a", "a"),
        ("ac", "a"),
        ("cbbd", "bb"),
        (f"a{'b'*1_000}c", 'b'*1_000)
    ]
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.longest_palindrome(inputs)

    assert actual == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ({"text": "bab", "idx": 1}, "bab"),
        ({"text": "bab", "idx": 0}, "b"),
        ({"text": "bad", "idx": 1}, "a"),
    ]
)
def test_palindrome_getter(inputs, expected):
    sut = Solution()

    actual = sut.get_palindrome_substring(inputs["text"], inputs["idx"])

    assert actual == expected
