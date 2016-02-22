class Solution(object):
    def findStrobogrammatic(self, n):
        self.n = n
        return self.helper(n)
    
    def helper(self, current):
        if current == 0:
            return ['']
        elif current == 1:
            return ['0', '1', '8']
        
        res = []
        
        for num in self.helper(current - 2):
            res.append('1' + num + '1')
            res.append('8' + num + '8')
            res.append('6' + num + '9')
            res.append('9' + num + '6')
            if current != self.n:
                res.append('0' + num + '0')
        
        return res
