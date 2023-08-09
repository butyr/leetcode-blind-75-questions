"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Difficulty: Medium
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l

            if nums[r] == target:
                return r

            mid = l + (r - l + 1) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[r]:
                if nums[mid] < target and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] and target > nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
