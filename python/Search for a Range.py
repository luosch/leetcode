class Solution(object):
    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return -1

    def searchRange(self, nums, target):
        m = len(nums)
        if m == 1:
            return [-1, -1] if nums[0] != target else [0, 0]

        spot = self.binarySearch(nums, 0, m - 1, target)

        if spot == -1:
            return [-1, -1]

        ans_start = ans_end = spot

        start = spot - 1
        start = self.binarySearch(nums, 0, start, target)

        while start > -1:
            ans_start = start
            start -= 1
            start = self.binarySearch(nums, 0, start, target)

        end = spot + 1
        end = self.binarySearch(nums, end, m - 1, target)

        while end > -1:
            ans_end = end
            end += 1
            end = self.binarySearch(nums, end, m - 1, target)

        return [ans_start, ans_end]
