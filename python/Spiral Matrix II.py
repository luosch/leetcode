class Solution(object):
    def generateMatrix(self, n):
        if n == 0:
            return []
        if n == 1:
            return [[1]]

        matrix = [[-1 for x in range(n)] for y in range(n)]
        direction = right
        current = 2
        pos_x = 0
        pos_y = 0
        matrix[0][0] = 1
        while current <= n * n:
            if direction == right:
                if pos_y + 1 >= n or matrix[pos_x][pos_y + 1] != -1:
                    direction = down
                else:
                    pos_y += 1
                    matrix[pos_x][pos_y] = current
                    current += 1
            elif direction == down:
                if pos_x + 1 >= n or matrix[pos_x + 1][pos_y] != -1:
                    direction = left
                else:
                    pos_x += 1
                    matrix[pos_x][pos_y] = current
                    current += 1
            elif direction == left:
                if pos_y - 1 < 0 or matrix[pos_x][pos_y - 1] != -1:
                    direction = up
                else:
                    pos_y -= 1
                    matrix[pos_x][pos_y] = current
                    current += 1
            elif direction == up:
                if pos_x - 1 < 0 or matrix[pos_x - 1][pos_y] != -1:
                    direction = right
                else:
                    pos_x -= 1
                    matrix[pos_x][pos_y] = current
                    current += 1
        
        return matrix
