"""
https://leetcode.com/problems/longest-palindromic-substring/
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

    def get_palindrome_substring(self, s: str, idx: int) -> str:
        curr_idx_left, curr_idx_right = self.get_idxs_around_center(s, idx)
        curr_substring = ""

        while curr_idx_left >= 0 and curr_idx_right < len(s):
            if s[curr_idx_left] == s[curr_idx_right]:
                curr_substring = s[curr_idx_left: curr_idx_right + 1]
            else:
                break

            curr_idx_left -= 1
            curr_idx_right += 1

        return curr_substring

    @staticmethod
    def get_idxs_around_center(s: str, idx: int) -> Tuple[int, int]:
        """
        Computes the starting indices around the palindrome center.
        Sometimes the center is not just a single character.
        For that case the indices need to be adjusted.

        :param s:
        :param idx:
        :return:
        """

        curr_idx_left = idx
        curr_idx_right = idx

        while curr_idx_left - 1 >= 0 and s[curr_idx_left - 1] == s[idx]:
            curr_idx_left -= 1

        while curr_idx_right + 1 < len(s) and s[curr_idx_right + 1] == s[idx]:
            curr_idx_right += 1

        return curr_idx_left, curr_idx_right
