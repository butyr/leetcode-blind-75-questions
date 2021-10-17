"""
https://leetcode.com/problems/contains-duplicate/

Runtime: 116 ms, faster than 85.68% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.9 MB, less than 88.15% of Python3 online submissions for Contains Duplicate.
"""


from typing import List


class Solution:
    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True

            num_set.add(num)

        return False
