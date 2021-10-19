"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        start_price = prices[0]
        max_profit = 0

        for curr_price in prices[1:]:
            max_profit = max(max_profit, curr_price - start_price)
            start_price = min(start_price, curr_price)

        return max_profit
