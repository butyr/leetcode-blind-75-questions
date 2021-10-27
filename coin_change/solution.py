"""
https://leetcode.com/problems/coin-change/

Difficulty: Medium
"""


from typing import List


class Solution:
    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        dp = {**{0: 0}, **{k: amount + 1 for k in range(1, amount + 1)}}

        for curr_amount in range(amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(
                        dp[curr_amount], dp[curr_amount - coin] + 1
                    )

        return dp[amount] if dp[amount] <= amount else -1
