class Solution(object):
    def generatePossibleNextMoves(self, s):
        n = len(s)

        if n == 0:
            return []
        
        ans = []

        for i in range(n - 1):
            if s[i] == s[i + 1] == +:
                    ans.append(%s--%s % (s[0:i], s[i+2:]))
        
        return ans
