import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ({"nums": [2, 7, 11, 15], "target": 9}, [1, 2]),
        ({"nums": [2, 3, 4], "target": 6}, [1, 3]),
        ({"nums": [-1, 0], "target": -1}, [1, 2]),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.two_sum(inputs["nums"], inputs["target"])

    assert actual == expected
