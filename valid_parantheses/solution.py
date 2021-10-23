"""
https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy
"""


class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        stack = []
        opening = "([{"
        close2open = {")": "(", "]": "[", "}": "{"}

        for s_i in s:
            if s_i in opening:
                stack.append(s_i)

            else:
                if len(stack) == 0 or close2open[s_i] != stack[-1]:
                    return False

                stack.pop()

        return len(stack) == 0
