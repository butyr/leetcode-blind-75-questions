"""
https://leetcode.com/problems/two-sum/

Runtime: 52 ms, faster than 97.49% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 41.59% of Python3 online submissions for Two Sum.
"""


from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        hash_map = {k: v for v, k in enumerate(nums)}

        for idx, num in enumerate(nums):
            if target - num in hash_map and hash_map[target - num] != idx:
                return [idx, hash_map[target - num]]

        return [-1, -1]
