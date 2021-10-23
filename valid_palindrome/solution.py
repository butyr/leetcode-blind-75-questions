"""
https://leetcode.com/problems/valid-palindrome

Difficulty: Easy
"""


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        inputs = [s_i.lower() for s_i in s if s_i.isalnum()]

        low = 0
        high = len(inputs) - 1

        while low < high:
            if inputs[low] != inputs[high]:
                return False

            low += 1
            high -= 1

        return True
