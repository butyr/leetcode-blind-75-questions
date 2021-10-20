"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


from typing import List


class Solution:
    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1
        while left_idx < right_idx:
            if target - numbers[left_idx] == numbers[right_idx]:
                return [left_idx + 1, right_idx + 1]

            elif target - numbers[left_idx] > numbers[right_idx]:
                left_idx += 1

            else:
                right_idx -= 1

        return [-1, -1]
