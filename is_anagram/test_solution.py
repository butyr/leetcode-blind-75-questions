import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ({"s": "anagram", "t": "nagaram"}, True),
        ({"s": "rat", "t": "car"}, False),
    ]
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.is_anagram(inputs["s"], inputs["t"])

    assert actual == expected
