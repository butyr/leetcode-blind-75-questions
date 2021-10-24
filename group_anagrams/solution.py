"""
https://leetcode.com/problems/group-anagrams/

Difficulty: Medium
"""


from typing import List


class Solution:
    @staticmethod
    def group_anagram(strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())
