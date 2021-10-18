"""
https://leetcode.com/problems/maximum-product-subarray/
"""


from typing import List


class Solution:
    @staticmethod
    def max_product(nums: List[int]) -> int:
        curr_prod = nums[0]
        max_prod = curr_prod

        for num in nums[1:]:
            curr_prod = max(curr_prod * num, num)
            max_prod = max(max_prod, curr_prod)

        return max_prod
