import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (int('00000000000000000000000000001011', 2), 3),
        (int('00000000000000000000000010000000', 2), 1),
        (int('11111111111111111111111111111101', 2), 31),
    ]
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.hamming_weight(inputs)

    assert actual == expected
