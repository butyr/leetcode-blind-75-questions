"""
https://leetcode.com/problems/number-of-1-bits/

Difficulty: Easy
"""


class Solution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        return sum([1 for n_i in "{0:b}".format(n) if n_i == "1"])
