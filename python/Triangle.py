class Solution(object):
    def minimumTotal(self, triangle):
        rows = len(triangle)
        current = prev = triangle[0]
        for i in range(1, rows):
            current = [0] * (i + 1)
            current[0] = triangle[i][0] + prev[0]
            current[-1] = triangle[i][-1] + prev[-1]
            for j in range(1, i):
                current[j] = triangle[i][j]
                current[j] += min(prev[j - 1], prev[j])
            prev = current
        return min(current)
