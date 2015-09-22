class Solution(object):
    def canPermutePalindrome(self, s):
        count = dict()
        for c in s:
            if not c in count:
                count.update({c: 1})
            else:
                count[c] += 1
        
        odd = 0
        for value in count.values():
            if value % 2:
                odd += 1
            if odd > 1:
                return False
        
        return True
