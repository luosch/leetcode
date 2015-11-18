from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        for i in xrange(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
