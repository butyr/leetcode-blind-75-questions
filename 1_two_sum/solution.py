from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        hash_map = {k: v for v, k in enumerate(nums)}

        for idx, n in enumerate(nums):
            if target-n in hash_map and hash_map[target-n] != idx:
                return [idx, hash_map[target-n]]
