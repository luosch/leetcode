class Solution(object):
    def countPrimes(self, n):
        if n == 0:
            return 0
        isPrime = [True] * (n + 1)
        isPrime[0] = isPrime[1] = False
        i = 2
        while i * i <= n:
            if isPrime[i]:
                k = i + i
                while k <= n:
                    isPrime[k] =False
                    k += i
            i += 1
        count = 0
        for i in range(1, n):
            if isPrime[i]:
                count += 1
        return count
