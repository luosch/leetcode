class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        import heapq
        q, ugly, k = [], [1], len(primes)
        for i in range(k):
            heapq.heappush(q, (primes[i], 0, primes[i]))
        for t in range(n - 1):
            x, i, p = q[0]
            ugly.append(x)
            while q and q[0][0] == x:
                x, i, p = heapq.heappop(q)
                heapq.heappush(q, (p * ugly[i + 1], i + 1, p))
        return ugly[-1]