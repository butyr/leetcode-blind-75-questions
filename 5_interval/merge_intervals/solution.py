"""
https://leetcode.com/problems/merge-intervals

Difficulty: Medium
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        if len(intervals) == 1:
            return intervals

        new_interval = intervals[0]
        updated_intervals = []

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if new_interval[1] < interval[0]:
                if len(updated_intervals) == 0:
                    updated_intervals += [new_interval] + [interval]
                else:
                    updated_intervals += [interval]
                new_interval = interval

            elif self.is_overlap(new_interval, interval):
                new_interval[1] = max(new_interval[1], interval[1])
                new_interval[0] = min(new_interval[0], interval[0])

                if len(updated_intervals) == 0:
                    updated_intervals = [new_interval]

                elif new_interval[0] > updated_intervals[-1][1]:
                    updated_intervals += [new_interval]
                else:
                    new_interval[0] = min(updated_intervals[-1][0], new_interval[0])
                    updated_intervals[-1] = new_interval

        return updated_intervals

    def is_overlap(self, new_interval, interval):
        return interval[1] >= new_interval[1] >= interval[0] or (
            new_interval[0] <= interval[0] and new_interval[1] >= interval[1]
        )
