class Solution(object):
    def titleToNumber(self, s):
        base = 1
        answer = 0
        for i in range(len(s) - 1, -1, -1):
            answer += (ord(s[i]) - ord('A') + 1) * base
            base *= 26
        return answer
        
