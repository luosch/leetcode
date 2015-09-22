class Solution(object):
    def hIndex(self, citations):
        left = 0
        right = len(citations) - 1
        n = len(citations)
        if n == 0 or citations[-1] <= 0:
            return 0
        while left < right:
            mid = (left + right) / 2
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid
        
        return n - (left + right) / 2
