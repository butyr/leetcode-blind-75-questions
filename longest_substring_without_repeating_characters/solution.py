"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


from typing import Dict


class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        max_len: int = 0
        index_map: Dict[str, int] = {}
        curr_substring: str = ""

        for i, s_i in enumerate(s):
            if s_i not in curr_substring:
                curr_substring += s_i
            else:
                curr_substring = s[index_map[s_i]+1: i+1]

            index_map[s_i] = i

            if len(curr_substring) > max_len:
                max_len = len(curr_substring)

        return max_len
