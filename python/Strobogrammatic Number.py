class Solution(object):
    def isStrobogrammatic(self, num):
        check = []
        for c in num:
            if c in '018':
                check.append(c)
            elif c == '6':
                check.append('9')
            elif c == '9':
                check.append('6')
        
        return ''.join(check) == num[::-1]
