class Solution(object):
    def rotate(self, matrix):
        matrix[:]=[[row[col] for row in matrix[::-1]] for col in range(len(matrix[::-1][0]))]
