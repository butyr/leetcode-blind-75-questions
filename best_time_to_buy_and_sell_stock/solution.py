"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Runtime: 920 ms, faster than 98.07% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 95.47% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""


from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        start_price = prices[0]
        max_profit = 0

        for curr_price in prices[1:]:
            if curr_price - start_price > max_profit:
                max_profit = curr_price - start_price

            if curr_price < start_price:
                start_price = curr_price

        return max_profit
