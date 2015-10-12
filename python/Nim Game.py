class Solution(object):
    def canWinNim(self, n):
        if n % 4:
            return True
        else:
            return False
        # return True if n % 4 else False
