class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        def bfs(x, y):
            queue = [(x, y)]
            visited = set()
            visited.add((x, y))
            while len(queue) != 0:
                ox, oy = queue[0]
                queue.pop(0)
                for dx, dy in [(ox, oy + 1), (ox, oy - 1), (ox + 1, oy), (ox - 1, oy)]:
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:
                        if rooms[dx][dy] not in [-1, 0]:
                            rooms[dx][dy] = min(rooms[dx][dy], rooms[ox][oy] + 1)
                            queue.append((dx, dy))
                            visited.add((dx, dy))
            
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i, j)
