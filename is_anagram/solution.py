"""
https://leetcode.com/problems/valid-anagram

Difficulty: Easy
"""


class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
