"""
https://leetcode.com/problems/climbing-stairs/

Difficulty: Easy
"""


class Solution:
    @staticmethod
    def climb_stairs(n: int) -> int:
        paths = {0: 1, 1: 1, 2: 2}

        for i in range(3, n + 1):
            paths[i] = paths[i - 1] + paths[i - 2]

        return paths[n]
