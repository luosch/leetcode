class Solution(object):
    def isStrobogrammatic(self, num):
        m = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        n = len(num)
        left, right = 0, n - 1
        while left <= right:
            if num[left] not in m or m[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def isStrobogrammatic_slow(self, num):
        check = []
        for c in num:
            if c in '018':
                check.append(c)
            elif c == '6':
                check.append('9')
            elif c == '9':
                check.append('6')
        
        return ''.join(check) == num[::-1]
