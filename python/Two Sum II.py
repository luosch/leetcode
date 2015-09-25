class Solution(object):
    def twoSum_slow(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            num = numbers[left] + numbers[right]
            
            if num == target:
                return [left + 1, right + 1]
            elif num < target:
                left += 1
            elif num > target:
                right -= 1
    
    def twoSum_slowest(self, numbers, target):
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif tmp < numbers[mid]:
                    right = mid - 1
                elif tmp > numbers[mid]:
                    left = mid + 1
    
    # dictionary           
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
