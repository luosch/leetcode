class Solution(object):
    dp = [0]
    def numSquares(self, n):
        if len(self.dp) <= n:
            tmp = [x**2 for x in range(1, int(math.sqrt(n)) + 1)]
            for i in range(len(self.dp), n + 1):
                self.dp.append(min(1 + self.dp[i - x] for x in tmp if x <= i))
        
        return self.dp[n]
