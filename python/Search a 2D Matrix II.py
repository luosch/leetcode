class Solution(object):
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return True

        return False


    def searchMatrix(self, matrix, target):
        m = len(matrix)

        for i in range(m):
            if self.binarySearch(matrix[i], target):
                return True

        return False
