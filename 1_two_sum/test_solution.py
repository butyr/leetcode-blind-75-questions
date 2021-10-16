import pytest
from solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ({"nums": [2, 7, 11, 15], "target": 9}, [0, 1]),
        ({"nums": [2, 11, 15, 7], "target": 9}, [0, 3]),
        ({"nums": [11, 2, 15, 7], "target": 9}, [1, 3]),
        ({"nums": [11, 1, 2, 15, 7], "target": 9}, [2, 4]),
        ({"nums": [11, 8, 2, 15, 7], "target": 9}, [2, 4]),
        ({"nums": [11, 2, 15, 7, 8], "target": 9}, [1, 3]),
        ({"nums": [3, 2, 4], "target": 6}, [1, 2]),
        ({"nums": [3, 3], "target": 6}, [0, 1]),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.two_sum(inputs["nums"], inputs["target"])

    assert actual == expected
