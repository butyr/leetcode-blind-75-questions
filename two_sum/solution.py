from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        hash_map = {k: v for v, k in enumerate(nums)}

        for idx, num in enumerate(nums):
            if target - num in hash_map and hash_map[target - num] != idx:
                return [idx, hash_map[target - num]]

        return [-1, -1]
