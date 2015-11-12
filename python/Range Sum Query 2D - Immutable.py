class NumMatrix(object):
    def __init__(self, matrix):
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        
        self.sum = []
        for row in matrix:
            tmp = [0] * len(row)
            tmp[0] = row[0]
            for i in range(1, len(row)):
                tmp[i] = tmp[i - 1] + row[i]
            self.sum.append(tmp)
        

    def sumRegion(self, row1, col1, row2, col2):
        answer = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                answer += self.sum[i][col2]
            else:
                answer += self.sum[i][col2] - self.sum[i][col1 - 1]
        return answer


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
