"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
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
