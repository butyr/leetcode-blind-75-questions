"""
https://leetcode.com/problems/maximum-subarray/

Difficulty: Easy
"""


from typing import List


class Solution:
    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum

        for num in nums[1:]:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
