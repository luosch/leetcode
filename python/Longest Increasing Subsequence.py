class Solution(object):
    def search(self, tmp, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if tmp[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return (right + left) // 2

    def lengthOfLIS(self, nums):
        tmp = []
        for num in nums:
            pos = self.search(tmp, 0, len(tmp), num)
            if pos >= len(tmp):
                tmp.append(num)
            else:
                tmp[pos] = num

        return len(tmp)
