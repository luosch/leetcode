# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        
        rooms = e = 0
        for start in starts:
            if start < ends[e]:
                rooms += 1
            else:
                e += 1
        
        return rooms
