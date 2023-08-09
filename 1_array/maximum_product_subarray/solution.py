"""
https://leetcode.com/problems/maximum-product-subarray/

Difficulty: Medium
"""


from typing import List


class Solution:
    @staticmethod
    def max_product(nums: List[int]) -> int:
        curr_min_prod = nums[0]
        curr_max_prod = nums[0]
        total_max_prod = max(nums)

        for num in nums[1:]:
            if num == 0:
                curr_min_prod, curr_max_prod = 1, 1

            else:
                last_min_prod = curr_min_prod
                curr_min_prod = min(curr_min_prod * num, curr_max_prod * num, num)
                curr_max_prod = max(curr_max_prod * num, last_min_prod * num, num)

                total_max_prod = max(total_max_prod, curr_max_prod)

        return total_max_prod
