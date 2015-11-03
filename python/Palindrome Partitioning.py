class Solution(object):
    def dfs(self, s, ans, tmp):
        if not s:
            ans.append(tmp)
        else:
            for i in range(len(s)):
                if s[:i + 1] == s[:i + 1][::-1]:
                    self.dfs(s[i + 1:], ans, tmp + [s[:i + 1]])
        
    def partition(self, s):
        ans = []
        self.dfs(s, ans, [])
        return ans
