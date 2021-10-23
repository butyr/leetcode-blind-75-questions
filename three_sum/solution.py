"""
https://leetcode.com/problems/3sum/
"""


from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        results = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            results += self.binary_search(nums, -1 * num, i)

        return results

    @staticmethod
    def binary_search(nums: List[int], target: int, idx: int) -> List[List[int]]:
        low = idx + 1
        high = len(nums) - 1
        results = []

        while low < high:
            if nums[low] + nums[high] < target:
                low += 1
            elif nums[low] + nums[high] > target:
                high -= 1

            else:
                if [nums[idx], nums[low], nums[high]] not in results:
                    results.append([nums[idx], nums[low], nums[high]])
                low += 1
                high -= 1

        return results
