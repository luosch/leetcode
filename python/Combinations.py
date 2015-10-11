class Solution(object):
    answer = []
    n = None
    def dfs(self, x, k, tmp):
        tmp = tmp[::]
        tmp.append(x)
        if k == 0:
            self.answer.append(tmp)
            return
        
        for i in range(x + 1, self.n - k + 2):
            self.dfs(i, k - 1, tmp)
        
    def combine(self, n, k):
        self.answer = []
        self.n = n
        
        for i in range(1, n - k + 2):
            self.dfs(i, k - 1, [])
        
        return self.answer
