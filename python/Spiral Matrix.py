class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = []
        used = [[False for x in range(n)] for y in range(m)]
        direction = "right"
        current = 0
        pos_x = 0
        pos_y = -1
        while current < m * n:
            if direction == "right":
                if pos_y + 1 >= n or used[pos_x][pos_y + 1]:
                    direction = "down"
                else:
                    pos_y += 1
                    used[pos_x][pos_y] = True
                    ans.append(matrix[pos_x][pos_y])
                    current += 1
            elif direction == "down":
                if pos_x + 1 >= m or used[pos_x + 1][pos_y]:
                    direction = "left"
                else:
                    pos_x += 1
                    used[pos_x][pos_y] = True
                    ans.append(matrix[pos_x][pos_y])
                    current += 1
            elif direction == "left":
                if pos_y - 1 < 0 or used[pos_x][pos_y - 1]:
                    direction = "up"
                else:
                    pos_y -= 1
                    used[pos_x][pos_y] = True
                    ans.append(matrix[pos_x][pos_y])
                    current += 1
            elif direction == "up":
                if pos_x - 1 < 0 or used[pos_x - 1][pos_y]:
                    direction = "right"
                else:
                    pos_x -= 1
                    used[pos_x][pos_y] = True
                    ans.append(matrix[pos_x][pos_y])
                    current += 1
        
        return ans
