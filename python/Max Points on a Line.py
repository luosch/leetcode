# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        answer = 0
        d = collections.defaultdict(int)
        for i in range(n):
            d.clear()
            overlap, curmax = 0, 0
            
            for j in range(i + 1, n):
                dx, dy = points[i].x - points[j].x, points[i].y - points[j].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                slope = float(dy) / float(dx) if dx != 0 else 'inf'
                d[slope] += 1
                curmax = max(curmax, d[slope])

            answer = max(answer, curmax + overlap + 1)
        return answer
