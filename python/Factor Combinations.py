class Solution(object):
    def getFactors(self, n):
        answer, stack, factor = [], [], 2
        while True:
            if factor > n / factor:
                if not stack:
                    return answer
                answer.append(stack + [n])
                factor = stack.pop()
                n *= factor
                factor += 1
            elif n % factor == 0:
                stack.append(factor)
                n /= factor
            else:
                factor += 1
    
    def getFactors_slow(self, n):
        self.res = []
        self.helper(2, n, [])
        return self.res[:-1]
        
    def helper(self, low, n, tmp):
        if n == 1:
            self.res.append(tmp)
            return
        
        for factor in range(low, int(n ** 0.5) + 1):
            if n % factor == 0:
                self.helper(factor, n / factor, tmp + [factor])
        
        self.helper(n, 1, tmp + [n])
