"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


from typing import Tuple


class Solution:
    def longest_palindrome(self, s: str) -> str:
        max_len = 0
        max_palindrome = ""

        for i in range(len(s)):
            curr_palindrome = self.get_palindrome_substring(s, i)
            if len(curr_palindrome) > max_len:
                max_len = len(curr_palindrome)
                max_palindrome = curr_palindrome

        return max_palindrome

    def get_palindrome_substring(self, input_string: str, center_idx: int) -> str:
        """
        Finds the palindrome with the maximal length under the assumption that center_idx is
        the center of the palindrome.

        :param input_string:
        :param center_idx:
        :return:
        """

        curr_idx_left, curr_idx_right = self.get_idxs_around_center(
            input_string, center_idx
        )
        curr_substring = ""

        while curr_idx_left >= 0 and curr_idx_right < len(input_string):
            if input_string[curr_idx_left] != input_string[curr_idx_right]:
                break

            curr_substring = input_string[curr_idx_left : curr_idx_right + 1]

            curr_idx_left -= 1
            curr_idx_right += 1

        return curr_substring

    @staticmethod
    def get_idxs_around_center(input_string: str, center_idx: int) -> Tuple[int, int]:
        """
        Computes the starting indices around the palindrome center.
        Sometimes the center is not just a single character.
        For that case the indices need to be adjusted.

        :param input_string:
        :param center_idx:
        :return:
        """

        curr_idx_left = center_idx
        curr_idx_right = center_idx

        while (
            curr_idx_left - 1 >= 0
            and input_string[curr_idx_left - 1] == input_string[center_idx]
        ):
            curr_idx_left -= 1

        while (
            curr_idx_right + 1 < len(input_string)
            and input_string[curr_idx_right + 1] == input_string[center_idx]
        ):
            curr_idx_right += 1

        return curr_idx_left, curr_idx_right
