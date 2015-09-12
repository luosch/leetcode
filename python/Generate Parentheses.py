class Solution(object):
    answer = []
    def dfs(self, left, right, paren):
        if left > right or left < 0 or right < 0:
            return
        
        if left == 0 and right == 0:
            self.answer.append(paren)
        
        self.dfs(left - 1, right, paren + '(')
        self.dfs(left, right - 1, paren + ')')
        
    def generateParenthesis(self, n):
        self.answer = []
        self.dfs(n, n, )
        return self.answer
