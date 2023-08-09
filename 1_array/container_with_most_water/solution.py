"""
https://leetcode.com/problems/container-with-most-water

Difficulty: Medium
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            new_area = self.get_area(height[l], height[r], l, r)
            max_area = max(new_area, max_area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_area

    def get_area(self, x, y, idx_left, idx_right):
        return min(x, y) * (idx_right - idx_left)
