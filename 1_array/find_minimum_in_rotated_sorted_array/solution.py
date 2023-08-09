"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Difficulty: Medium
"""


from typing import List


class Solution:
    @staticmethod
    def findMin(nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if len(nums[l : r + 1]) == 1:
                return nums[l]

            if len(nums[l : r + 1]) == 2:
                return min(nums[l : r + 1])

            mid = l + (r - l + 1) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
