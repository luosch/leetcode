class Solution(object):
    res = []
    def binary_search(self, left, right):
        if left == right:
            return self.res[left]
        elif left + 1 == right:
            return min(self.res[left], self.res[right])
        else:
            mid = (left + right) / 2
            if self.res[mid - 1] > self.res[mid] < self.res[mid + 1]:
                return self.res[mid]
            else:
                return min(self.binary_search(left, mid - 1), self.binary_search(mid + 1, right))
        
    def findMin(self, nums):
        self.res = nums
        return self.binary_search(0, len(nums) - 1)
