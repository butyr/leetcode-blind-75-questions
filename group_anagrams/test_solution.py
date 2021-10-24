from typing import List

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
    ],
)
def test_solution(inputs, expected):
    sut = Solution()

    actual = sut.group_anagram(inputs)

    assert normalize(actual) == normalize(expected)


def normalize(anagrams: List[List[str]]) -> List[List[str]]:
    anagrams = [sorted(anagram) for anagram in anagrams]
    anagrams = sorted(anagrams)

    return anagrams
