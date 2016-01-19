import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num):
        num = float(num)
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        
        if num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) - len(self.small) == 2:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return -self.small[0] if len(self.small) > len(self.large) else self.large[0]
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
