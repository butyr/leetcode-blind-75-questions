"""
https://leetcode.com/problems/longest-palindromic-substring/

Runtime: 1468 ms, faster than 43.77% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 81.09% of Python3 online submissions for Longest Palindromic Substring.
"""


from typing import Tuple


class Solution:
    def longest_palindrome(self, s: str) -> str:
        max_len = 0
        max_palindrome = ""

        for i in range(len(s)):
            curr_substring = self.get_palindrome_substring(s, i)
            if len(curr_substring) > max_len:
                max_len = len(curr_substring)
                max_palindrome = curr_substring

        return max_palindrome

    def get_palindrome_substring(self, input_string: str, idx: int) -> str:
        curr_idx_left, curr_idx_right = self.get_idxs_around_center(input_string, idx)
        curr_substring = ""

        while curr_idx_left >= 0 and curr_idx_right < len(input_string):
            if input_string[curr_idx_left] == input_string[curr_idx_right]:
                curr_substring = input_string[curr_idx_left: curr_idx_right + 1]
            else:
                break

            curr_idx_left -= 1
            curr_idx_right += 1

        return curr_substring

    @staticmethod
    def get_idxs_around_center(input_string: str, idx: int) -> Tuple[int, int]:
        """
        Computes the starting indices around the palindrome center.
        Sometimes the center is not just a single character.
        For that case the indices need to be adjusted.

        :param input_string:
        :param idx:
        :return:
        """

        curr_idx_left = idx
        curr_idx_right = idx

        while (
            curr_idx_left - 1 >= 0
            and input_string[curr_idx_left - 1] == input_string[idx]
        ):
            curr_idx_left -= 1

        while (
            curr_idx_right + 1 < len(input_string)
            and input_string[curr_idx_right + 1] == input_string[idx]
        ):
            curr_idx_right += 1

        return curr_idx_left, curr_idx_right
