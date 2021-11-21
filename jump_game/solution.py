"""
https://leetcode.com/problems/jump-game/

Difficulty: Medium
"""


from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        min_pos = len(nums) - 1

        for curr_pos in range(len(nums)-2, -1, -1):
            if curr_pos + nums[curr_pos] >= min_pos:
                min_pos = curr_pos

        return min_pos == 0
