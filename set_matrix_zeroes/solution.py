"""
https://leetcode.com/problems/set-matrix-zeroes/

Difficulty: Medium
"""


from typing import List


class Solution:
    @staticmethod
    def set_zeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows = [False] * len(matrix)
        zero_cols = [False] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows[row], zero_cols[col] = True, True

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if zero_cols[col] or zero_rows[row]:
                    matrix[row][col] = 0
