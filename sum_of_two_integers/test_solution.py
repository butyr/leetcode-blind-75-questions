import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ({"a": 1, "b": 2}, 3),
        ({"a": 2, "b": 3}, 5),
        ({"a": -1, "b": 1}, 0),
        ({"a": -3, "b": 2}, -1),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.get_sum(inputs["a"], inputs["b"])

    assert actual == expected
