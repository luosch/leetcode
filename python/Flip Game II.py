class Solution(object):
    def canWin(self, s):
        return any(not self.canWin(s[:i]+"--"+s[i+2:]) for i in xrange(len(s)-1) if s[i:i+2] == "++")
