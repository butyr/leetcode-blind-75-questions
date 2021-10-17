"""
https://leetcode.com/problems/product-of-array-except-self/

Runtime: 220 ms, faster than 98.82% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.3 MB, less than 42.61% of Python3 online submissions for Product of Array Except Self.
"""


from typing import List


class Solution:
    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        num_zeros = len([1 for num in nums if num == 0])

        if num_zeros > 1:
            return [0] * len(nums)

        if num_zeros == 1:
            product = 1
            zero_idx = 0
            for idx, num in enumerate(nums):
                if num != 0:
                    product *= num
                else:
                    zero_idx = idx

            result = [0] * len(nums)
            result[zero_idx] = product

            return result

        product = 1
        for num in nums:
            product *= num

        results = []
        for num in nums:
            results.append(product // num)

        return results
