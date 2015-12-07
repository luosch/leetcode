# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda item:item.start)
        answer = [intervals[0]]
        for item in intervals[1:]:
            if item.start > answer[-1].end:
                answer.append(item)
            else:
                answer[-1].end = max(answer[-1].end, item.end)
        return answer
