class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        else:
            base = self.grayCode(n - 1)
            return [num for num in base] + [2 ** (n-1) + num for num in base[::-1]]
