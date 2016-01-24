class Solution(object):
    def minTotalDistance(self, grid):
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        px = [i for j in range(n) for i in range(m) if grid[i][j]]
        py = [j for j in range(n) for i in range(m) if grid[i][j]]
        
        px.sort()
        py.sort()
        sx = px[len(px) / 2]
        sy = py[len(py) / 2]
        
        return sum([abs(sx - p) for p in px]) + sum([abs(sy - p) for p in py])
