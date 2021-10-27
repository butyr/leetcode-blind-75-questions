import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ({"coins": [1, 2, 5], "amount": 11}, 3),
        ({"coins": [2], "amount": 3}, -1),
        ({"coins": [1], "amount": 0}, 0),
        ({"coins": [2, 5, 10, 1], "amount": 27}, 4),
        ({"coins": [186, 419, 83, 408], "amount": 6249}, 20),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.coin_change(inputs["coins"], inputs["amount"])

    assert actual == expected
