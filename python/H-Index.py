class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)
        for num in citations:
            if num > n:
                count[n] += 1
            else:
                count[num] += 1
        
        for i in range(n, 0, -1):
            if count[i] >= i:
                return i
            else:
                count[i - 1] += count[i]
        
        return 0
