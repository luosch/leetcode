class Solution(object):
    def searchMatrix(self, matrix, target):
        pos_x = 0
        pos_y = len(matrix[0]) - 1
        m = len(matrix)
        n = len(matrix[0])
        
        while 0 <= pos_x < m and 0 <= pos_y < n:
            if target < matrix[pos_x][pos_y]:
                pos_y -= 1
            elif target > matrix[pos_x][pos_y]:
                pos_x += 1
            else:
                return True
        
        return False
