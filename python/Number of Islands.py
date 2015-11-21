class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        answer = 0
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            
            if grid[x][y] == '1':
                grid[x][y] = 'x'
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '1':
                    continue
                else:
                    answer += 1
                    dfs(i, j)
        
        return answer
