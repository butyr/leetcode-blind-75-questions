"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


from typing import List


class Solution:
    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            if target - numbers[low] == numbers[high]:
                return [low + 1, high + 1]

            if target - numbers[low] > numbers[high]:
                low += 1
            else:
                high -= 1

        return [-1, -1]
