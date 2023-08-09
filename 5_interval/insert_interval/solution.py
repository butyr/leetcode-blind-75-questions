"""
https://leetcode.com/problems/insert-interval

Difficulty: Easy
"""


from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        updated_interval = []

        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                return updated_interval + [newInterval] + intervals[i:]

            elif interval[1] < newInterval[0]:
                updated_interval += [intervals[i]]

            if interval[1] >= newInterval[0] >= interval[0]:
                newInterval[0] = min(interval[0], newInterval[0])

            if interval[0] <= newInterval[1] <= interval[1]:
                newInterval[1] = max(interval[1], newInterval[1])

        return updated_interval + [newInterval]
