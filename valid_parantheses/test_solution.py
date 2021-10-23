import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("{[]}", True),
        ("[[}}", False),
    ]
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.is_valid(inputs)

    assert actual == expected
