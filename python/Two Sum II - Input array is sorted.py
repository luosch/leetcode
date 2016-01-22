class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)

        def binarySearch(left, right, value):
            while left <= right:
                mid = left + (right - left) / 2
                if numbers[mid] == value:
                    return mid
                elif numbers[mid] < value:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        for index1, value in enumerate(numbers):
            if target - value >= value:
                index2 = binarySearch(index1 + 1, n - 1, target - value)
                if index2 != -1:
                    return (index1 + 1, index2 + 1)
