"""
https://leetcode.com/problems/group-anagrams/

Difficulty: Medium
"""


from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def group_anagram(strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anagrams["".join(sorted(s))].append(s)

        return list(anagrams.values())
